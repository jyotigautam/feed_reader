# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import feedparser
import pdb
from django.views.generic.base import View


class HomeView(View):

    def get(self, request, *args, **kwargs):
        search = ""
        context = {}
        if request.GET.get('search'):
            search = request.GET.get('search').strip()
            feed = feedparser.parse(search)

            if hasattr(feed['feed'], 'title'):
                feed_title = feed['feed']['title']
            else:
                feed_title = "No feeds to show"

            if hasattr(feed['feed'], 'image'):
                feed_image = feed['feed']['image']['href']
            elif hasattr(feed['feed'], 'gd_image'):
                feed_image = feed['feed']['gd_image']['src']
            else:
                feed_image = None

            context = {
                'entries': feed.entries,
                'feed_title': feed_title,
                'feed_image': feed_image,
                'search': search
            }
        return render(request, 'index.html', context=context)
