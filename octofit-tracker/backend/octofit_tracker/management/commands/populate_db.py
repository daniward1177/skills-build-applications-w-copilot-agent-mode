from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data (delete individually for Djongo compatibility)
        for model in [Activity, Workout, Leaderboard, User, Team]:
            for obj in model.objects.all():
                if getattr(obj, 'id', None):
                    obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=timezone.now().date())

        # Create Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        workout2 = Workout.objects.create(name='Squats', description='Lower body strength')
        workout1.suggested_for.set([users[0], users[2]])
        workout2.suggested_for.set([users[1], users[3]])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, score=150)
        Leaderboard.objects.create(team=dc, score=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
