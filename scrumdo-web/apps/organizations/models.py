# ScrumDo - Agile/Scrum story management web application 
# Copyright (C) 2011 ScrumDo LLC
# 
# This software is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy (See file COPYING) of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


from django.core.urlresolvers import reverse
from django.contrib.auth.models import  User
from django.utils.translation import ugettext_lazy as _
from django.db import models

import datetime

from django.core.exceptions import ObjectDoesNotExist


# Was going to make these pinax groups, but didn't want to bring over the slug based urls for teams, and turns out organizations don't 
# actually have members if we go the team route.

class Organization(models.Model):   
  name = models.CharField( max_length=65 )
  slug = models.SlugField(_('slug'), unique=True)
  creator = models.ForeignKey(User, verbose_name=_('creator'), related_name="organizations_created")
  created = models.DateTimeField(_('created'), default=datetime.datetime.now)
  description = models.TextField(_('description'))
  
  def getDefaultTeam():
    return Organization.objects.filter( teams__access_type="admin", teams__members__user__id = user.id ).order_by("name")[0]
  
  # Returns all organizations
  @staticmethod
  def getOrganizationsForUser( user ):
    return Organization.objects.filter( teams__members = user ).distinct().order_by("name")

  # Returns all organizations the user has admin rights to.
  @staticmethod
  def getAdminOrganizationsForUser( user ):
    return Organization.objects.filter( teams__access_type="admin", teams__members = user ).distinct().order_by("name")


  # returns all organizations the user has read/write access to
  # @staticmethod
  # def getReadWriteOrganizationsForUser( user ):
  #   return Organization.objects.filter( teams__members = user ).exclude(teams__access_type = "read").distinct().order_by("name")


    
  def get_url_kwargs(self):
      return {'organization_slug': self.slug}



