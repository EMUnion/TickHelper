from mcdreforged.api.command import SimpleCommandBuilder
from mcdreforged.api.rcon import RconConnection as rcon
from mcdreforged.mcdr_server import ServerInterface


PLUGIN_METADATA = {
    'id': 'tick_helper',
    'version': '1.0.0',
    'name': 'TickHelper',
    'description': 'A plugin for users to use /tick freeze and /tick health command when carpet.tickCommand is set to ops',
    'author': 'GamerNoTitle',
    'link': 'https://github.com/EMUnion/TickHelper',
    'dependencies': {
        'mcdreforged': '>=2.6.0'
    }
}

global_freeze = False
global_server = ServerInterface.get_instance().as_plugin_server_interface()
help = '''{:=^50}
§b!!tick help §r- §6显示帮助信息
§b!!tick freeze §r- §6停止tick流动
§b!!tick status §r- §6查看tick状态
§b!!tick health §r- §6查看tick占用情况（目前无效，正在找解决方法）
{:=^50}'''.format(' §b[TickHelper] 帮助信息 §r', ' §b[TickHelper] Version: {} §r'.format(PLUGIN_METADATA['version']))
# r = rcon('127.0.0.1', 28584, 'EMUnion@EFS&MTS')

def freeze(source: ServerInterface):
    global_server.execute('/tick freeze')
    global global_freeze
    if not global_freeze:
        global_server.say('§b[TickHelper] §6スタープラチナ·The World！')
    else:
        global_server.say('§b[TickHelper] §6時は流れ続ける！')
    global_freeze = not global_freeze


def health(source: ServerInterface):
    # try:
    #     r.connect()
    #     text = r.send_command('tick health')
    #     r.disconnect()
    # except Exception as e:
    #     text = f'§b[TickHelper] §6无法查询tick health，因为发生了 {e} 错误！'
    text = '§b[TickHelper] §6无法查询tick health，因为发生这个功能还没有恰当的解决方案！'
    source.reply(text)


def help_msg(source):
    source.reply(help)

def status(source):
    if global_freeze:
        source.reply('§b[TickHelper] §6这个世界正在白金之星的影响之下！')
    else:
        source.reply('§b[TickHelper] §6时间正常流动，没有受到替身技能的影响~')

def on_load(server, prev):
    server.register_help_message('!!tick', 'TickHelper 帮助')
    builder = SimpleCommandBuilder()

    builder.command('!!tick', help_msg)
    builder.command('!!tick freeze', freeze)
    builder.command('!!tick health', health)
    builder.command('!!tick status', status)

    builder.register(server)


def on_unload(server):
    if global_freeze:
        server.say('§b[TickHelper] §6这个世界的替身突然间消失了，所有受到替身影响的状况都不翼而飞了~')
        freeze(server)
