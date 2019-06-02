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
            search = request.GET.get('search')
            feed = feedparser.parse(search)
            if hasattr(feed['feed'], 'image'):
                feed_image = feed['feed']['image']['href']
            else:
                feed_image = feed['feed']['gd_image']['src']

            context = {
                'entries': feed.entries,
                'feed_title': feed['feed']['title'],
                'feed_image': feed_image,
                'search': search
            }
        return render(request, 'index.html', context=context)
