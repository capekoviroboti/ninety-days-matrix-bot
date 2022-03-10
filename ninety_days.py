'''
ninety_days - A maubot plugin that calculates ninety days from a date.
'''
import datetime
from typing import Optional
from maubot import Plugin, MessageEvent
from maubot.handlers import command

DESC = 'Lookup 90 days from date.'
USAGE = 'Usage: !90days [<date>]. Date should be in the form YYYY-MM-DD.'
HELP_STR = f'{DESC} {USAGE}'


class NinetyDaysBot(Plugin):
    '''
    Compute ninety days from a date.
    '''
    @staticmethod
    def _ninety_days(d: str) -> str:
        try:
            return str(
                datetime.datetime.strptime(d, '%Y-%m-%d') +
                datetime.timedelta(days=90)
            )
        except BaseException:
            return ''

    @staticmethod
    def _no_args() -> str:
        return NinetyDaysBot._ninety_days(
            datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        )

    @command.new('90days', help=HELP_STR)
    @command.argument('date_str', pass_raw=True, required=False)
    async def handler(self, evt: MessageEvent, date_str: Optional[str]) -> None:
        '''Handler for bare call.'''
        await evt.mark_read()
        if date_str:
            result = NinetyDaysBot._ninety_days(date_str)
        else:
            result = NinetyDaysBot._no_args()
        await evt.reply(f'{result}', allow_html=True)
