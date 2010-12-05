from django.conf.urls.defaults import *

from projects.models import Project

# from groups.bridge import ContentBridge
# 
# 
# bridge = ContentBridge(Project, 'projects')

urlpatterns = patterns('projects.views',
    url(r'^$', 'projects', name="project_list"),
    url(r'^create/$', 'create', name="project_create"),
    url(r'^your_projects/$', 'your_projects', name="your_projects"),
    url(r'^project/(?P<group_slug>[-\w]+)/$', 'project', name="project_detail"),
    url(r'^project/(?P<group_slug>[-\w]+)/delete/$', 'delete', name="project_delete"),
    url(r'^project/(?P<group_slug>[-\w]+)/admin$', 'project_admin', name="project_admin"),
    url(r'^project/(?P<group_slug>[-\w]+)/fix_local_id$', 'fix_local_id', name="fix_local_id"),
    url(r'^project/(?P<group_slug>[-\w]+)/history$', 'project_history', name="project_history"),    
    url(r'^project/(?P<group_slug>[-\w]+)/test_data/(?P<count>[0-9]+)', 'test_data'),    
    
    url(r'^project/(?P<group_slug>[-\w]+)/(?P<iteration_id>[-\w]+)/burndown$', 'iteration_burndown'),    
    url(r'^project/(?P<group_slug>[-\w]+)/burndown$', 'project_burndown'),    
    url(r'^project/(?P<group_slug>[-\w]+)/project_prediction$', 'project_prediction', name="project_prediction"),    
)

urlpatterns += patterns('projects.iteration_views',
    url(r'^project/(?P<group_slug>[-\w]+)/iteration_create$', 'iteration_create', name="iteration_create"),
    url(r'^project/(?P<group_slug>[-\w]+)/iteration/(?P<iteration_id>[-\w]+)$', 'iteration', name="iteration"),
)


urlpatterns += patterns('projects.story_views',
    url(r'^project/(?P<group_slug>[-\w]+)/stories/$', 'stories', name="stories"),
    url(r'^project/(?P<group_slug>[-\w]+)/stories/(?P<iteration_id>[-\w]+)$', 'stories_iteration', name="stories_iteration"),
    url(r'^project/(?P<group_slug>[-\w]+)/story/(?P<story_id>[-\w]+)/pretty', 'pretty_print_story'),
    url(r'^project/(?P<group_slug>[-\w]+)/story/(?P<story_id>[-\w]+)/set_todo', 'set_story_status', {'status':1}),
    url(r'^project/(?P<group_slug>[-\w]+)/story/(?P<story_id>[-\w]+)/set_doing', 'set_story_status', {'status':2}),
    url(r'^project/(?P<group_slug>[-\w]+)/story/(?P<story_id>[-\w]+)/set_reviewing', 'set_story_status', {'status':3}),
    url(r'^project/(?P<group_slug>[-\w]+)/story/(?P<story_id>[-\w]+)/set_done', 'set_story_status', {'status':4}),
    url(r'^project/(?P<group_slug>[-\w]+)/story/(?P<story_id>[-\w]+)/reorder', 'reorder_story'),
    url(r'^project/(?P<group_slug>[-\w]+)/story/(?P<story_id>[-\w]+)/delete', 'delete_story', name="delete_story"),
    url(r'^project/(?P<group_slug>[-\w]+)/story/(?P<story_id>[-\w]+)', 'story', name="story_form"),
    url(r'^project/(?P<group_slug>[-\w]+)/mini_story/(?P<story_id>[-\w]+)', 'mini_story'),    
    url(r'^project/(?P<group_slug>[-\w]+)/import','import_file', name="import_file"),
    
)

# urlpatterns += bridge.include_urls('tasks.urls', r'^project/(?P<group_slug>[-\w]+)/tasks/')
