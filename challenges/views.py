


from __future__ import annotations

import random
from datetime import date  # type: ignore

from django.http import HttpResponseRedirect  # type: ignore
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render  # type: ignore
from django.urls import reverse  # type: ignore

# Create your views here.


# Month-specific realistic goal pools
GOALS : dict[str , list[str]] = {
    "january": [
        "Write a one-page personal strategy for the year and pick 3 priorities.",
        "Declutter your workspace and set up a weekly review routine.",
        "Commit to a 20-minute daily walk for the whole month.",
        "Define a simple budget and track every expense this month."
    ],
    "february": [
        "Have two focused deep-work sessions per week (no notifications).",
        "Plan a mini-getaway or local day trip before spring.",
        "Do a 14-day sugar reduction challenge.",
        "Reconnect with two old friends via a call or coffee."
    ],
    "march": [
        "Start a weekend routine to prep healthy lunches for the week.",
        "Read one practical non-fiction book and take notes.",
        "Plant herbs or a small balcony garden.",
        "Organize all important documents in cloud folders."
    ],
    "april": [
        "Do a 7-day digital detox after 9pm.",
        "Audit subscriptions and cancel at least two you barely use.",
        "Update your resume/portfolio with one new project.",
        "Volunteer for a local community activity once this month."
    ],
    "may": [
        "Wake up 30 minutes earlier for 10 weekdays in a row.",
        "Complete a 5K walk/run (or equivalent cycling distance).",
        "Create a simple meal plan with 3 go-to dinners.",
        "Back up your phone and laptop, and enable automatic backups."
    ],
    "june": [
        "Take one full unplugged weekend day outdoors.",
        "Batch-cook and freeze three healthy meals.",
        "Launch a tiny side project or publish a blog post.",
        "Review your mid-year goals and adjust one key metric."
    ],
    "july": [
        "Try a new hobby class (swim, dance, pottery, anything fun!).",
        "Host a simple gathering or picnic with friends/family.",
        "Replace sugary drinks with water or tea on weekdays.",
        "Do a photo cleanup: delete/organize 500 old photos."
    ],
    "august": [
        "Plan and book one experience you’ve postponed all year.",
        "Read for 20 minutes every night for two weeks.",
        "Streamline your morning routine to three steps.",
        "Do a finances check-in: set an automated monthly transfer to savings."
    ],
    "september": [
        "Enroll in a short online course and finish one module per week.",
        "Set up a weekly planning session every Sunday evening.",
        "Create a minimalist wardrobe list for workdays.",
        "Journal three times a week about energy and focus."
    ],
    "october": [
        "Prepare a simple emergency kit and contact list.",
        "Cook at home 5 nights in one week.",
        "Practice public speaking: record a 3-minute talk and review it.",
        "Do a social media fast for 48 hours."
    ],
    "november": [
        "List 10 things you’re grateful for each day for one week.",
        "Complete a 10-day pushup/plank or yoga challenge.",
        "Ship a small improvement at work or in your main project.",
        "Donate items you haven’t used in a year."
    ],
    "december": [
        "Do a year-in-review and archive your best notes & photos.",
        "Write thank-you messages to five people who helped you this year.",
        "Pick a single theme/word for next year.",
        "Set up a clean slate: inbox zero + task list reset."
    ],
}
def pick_goal(goal_key : str) ->str:
   return random.choice(GOALS[goal_key])

def pick_goal_by_number(goal_index:int)->str :
    values = list(GOALS.values())
    return random.choice(values[goal_index])
def get_month_by_number(goal_index:int)->str :
    return list(GOALS.keys())[goal_index-1]

def monthly_challenge_by_number(request: HttpRequest , month:int)->HttpResponse:
    if month <1 or month > len(GOALS):
        return HttpResponseNotFound("<h2>Wrong month number</h2>")
    redirect_path = reverse('month_challenge'  , args=[get_month_by_number(month)])
    return redirect(redirect_path)

def monthly_challenge(request:HttpRequest , month:str)->HttpResponse:
    month = month.lower()
    if month not in GOALS.keys():
        return HttpResponseNotFound('<h1>Wrong month name</h1>')
    response_data = f"<h1>{pick_goal(month)}</h1>"
    return HttpResponse(response_data)

def index(request:HttpRequest):
    links = ""
    for month in list(GOALS.keys()) :
        links = links + f"""
        <li>
        <a href="{reverse('month_challenge' , args=[month])}">{month.capitalize()}</a>
        </li>
        """
    body = f"""
    <ul>
    {links}
    </ul>
    """
    return HttpResponse(body)
