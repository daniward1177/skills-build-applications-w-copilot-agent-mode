from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2023-01-01')
        self.assertEqual(str(activity), 'Test User - Run on 2023-01-01')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertIn('Test Team', str(leaderboard))
