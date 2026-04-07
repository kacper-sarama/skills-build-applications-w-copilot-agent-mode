from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='ironman@marvel.com', activity_type='run', duration=30, date=timezone.now()),
            Activity(user='spiderman@marvel.com', activity_type='cycle', duration=45, date=timezone.now()),
            Activity(user='batman@dc.com', activity_type='swim', duration=60, date=timezone.now()),
            Activity(user='wonderwoman@dc.com', activity_type='yoga', duration=50, date=timezone.now()),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=200)
        Leaderboard.objects.create(team='dc', points=180)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Squats', description='Do 30 squats', difficulty='medium'),
            Workout(name='Plank', description='Hold plank for 1 min', difficulty='hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
