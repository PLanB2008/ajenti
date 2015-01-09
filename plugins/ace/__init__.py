from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='Ace editor',
    icon='cog',
    dependencies=[
        PluginDependency('core'),
    ],
    resources=[
        'resources/css/ace.less',

        'resources/js/module.coffee',

        'resources/js/directives/ace.coffee',
        
        'resources/vendor/ace-builds/src-min-noconflict/ace.js',
        'resources/vendor/ace-builds/src-min-noconflict/ext-modelist.js',
        'resources/vendor/ace-builds/src-min-noconflict/ext-themelist.js',
        'resources/vendor/ace-builds/src-min-noconflict/ext-settings_menu.js',
        'resources/vendor/ace-builds/src-min-noconflict/ext-language_tools.js',
        'resources/vendor/ace-builds/src-min-noconflict/theme-solarized_dark.js',
        'resources/vendor/angular-ui-ace/ui-ace.js',
    
        'ng:util.ace',
    ],
)


def init():
    pass
    