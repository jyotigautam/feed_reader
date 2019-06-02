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
            # pdb.set_trace()
            if hasattr(feed['feed'], 'image'):
                feed_image = feed['feed']['image']['href']
            elif hasattr(feed['feed'], 'gd_image'):
                feed_image = feed['feed']['gd_image']['src']
            else:
                feed_image = None

            context = {
                'entries': feed.entries,
                'feed_title': feed['feed']['title'],
                'feed_image': feed_image,
                'search': search
            }
        return render(request, 'index.html', context=context)
