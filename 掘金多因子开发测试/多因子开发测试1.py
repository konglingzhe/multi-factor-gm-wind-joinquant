from gm.api import *

BACKTEST_START_TIME = '2017-02-27'  # 回测开始日期
BACKTEST_END_TIME = '2018-06-14'  # 回测结束日期
INDEX = 'SHSE.000016'  # 股票池代码


def init(context):
    # 按照回测的将股票池的历史股票组成提出并合并
    history_constituents = get_history_constituents(INDEX, start_date=BACKTEST_START_TIME, end_date=BACKTEST_END_TIME)
    history_constituents = [set(temp['constituents'].keys()) for temp in history_constituents]
    history_constituents_all = set()
    for temp in history_constituents:
        history_constituents_all = history_constituents_all | temp
    history_constituents_all = list(history_constituents_all)
    # 根据板块的历史数据组成订阅数据
    subscribe(symbols=history_constituents_all, frequency='1d')
    # 每天14:50 定时执行algo任务
    schedule(schedule_func=algo, date_rule='daily', time_rule='14:50:00')


def algo(context):
    # 购买200股浦发银行股票
    order_volume(symbol='SHSE.600000', volume=200, side=1,
                 order_type=2, position_effect=1, price=0)


# 查看最终的回测结果
def on_backtest_finished(context, indicator):
    print(indicator)


if __name__ == '__main__':
    run(strategy_id='efed2881-7511-11e8-8fe1-305a3a77b8c5',
        filename='多因子开发测试1.py',
        mode=MODE_BACKTEST,
        token='d7b08e7e21dd0315a510926e5a53ade8c01f9aaa',
        backtest_start_time=BACKTEST_START_TIME+' 13:00:00',
        backtest_end_time=BACKTEST_END_TIME+' 15:00:00')