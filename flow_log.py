#coding=utf-8
import re
from collections import defaultdict
from pandas import DataFrame,concat,merge
from numpy import array,arange,concatenate
import traceback
from stats_utils import draw4
import constants

def main():
    try:

        with open(constants.DIR_LOG) as file:

            text = file.read()
            apipat = re.compile(constants.RE_API,re.S)
            content = re.findall(apipat,text)
            df = DataFrame(content,columns=['api','time'])
            df['time'] = df['time'].astype('int')
            points = getApiPoints(df)
            #x,y =array([1,1,1,1,1,1]),array([2,30,32,30,100,30])
            draw4(points['X'],points['Y'])

            """
            未展示的功能:

            打印所有统计结果

            from stats_utils import statistics
            res = statistics(df,'api','time')
            print res

            获取 前20% 统计结果

            print '按时间排序 前20% 的统计结果，按升序排列是:'
            print getPreRateData(df,0.2,'time',True)
            print '按时间排序 前20% 的统计结果，按降序排列是:'
            print getPreRateData(df,0.2,'time',False)

            获取 后20% 统计结果

            print '按时间排序 后20% 的统计结果，按升序排列是:'
            print getPostRateData(df,0.2,'time',True)
            print '按时间排序 后20% 的统计结果，按降序排列是:'
            print getPostRateData(df,0.2,'time',False)
            """
    except Exception:
        print traceback.format_exc()


def getApiPoints(df):
    """Generate Points data from the DataFrame .


    Args:
        df: a dataframe object which contains attributes named 'api' and 'time'

    Returns:
        A dict mapping keys to the corresponding row data fetched. Each row is represented as an array of floats.
        Keys are limited to the collection of {'X','Y'}.
        example:

        {'X':array([1.0,3.0,4.0]),
         'Y':array([323.0,542.0,234.0])}
    """
    if df.empty:
        return

    dfggc= df[df.api=='/bmis/v1_0/order/getOrderCount'].sort(columns=['time'],ascending=False)
    dfggn = df[df.api=='/bmis/v1_0/user/getGroupName'].sort(columns=['time'],ascending=False)
    apis = merge(dfggc,dfggn,on=['api','time'],how='outer')
    lstapi = [(dfggc,constants.POINTS_X_GET_ORDER_COUNT),(dfggn,constants.POINTS_X_GET_GROUP_NAME)]  # [(objapi,numapiX),]

    print '********api**********'
    print apis
    print '********api end******'

    def getXYs(dfapi,colstats,apiX):
        """Get x,y of points.

        Args:
            dfapi: a specific 'api' dateframe.
            colstats: an important column in the dataframe needed to be stated from which we need get the X,Y info of points.
            apiX: a contant string defined in constant.py used to mark a certain api. In other words, the same api should have the same x asix.

        Returns:
            Two array, say, X and Y. Each of these two array concatenate axis of the different apis. For
            example:

            {'X':array([1,1,1,1,2,2,2]),
             'Y':array([2.0,23.0,23.0,8.0,2.0,12.0,20.0])}

i       Raises:
            TypeError: An error occurred first accessing the null array in dict.
        """

        lst =[]
        map(lambda l: lst.append(apiX),arange(len(dfapi)))
        X, Y = array(lst), array(api[colstats])

        return X,Y

    points = defaultdict(array)

    for api,apiX in lstapi:

        X,Y = getXYs(api,'time',apiX)

        try:
            # 无异常则不是第一次循环,此时分别连接array
            points['X'] = concatenate((points['X'],X))
            points['Y'] = concatenate((points['Y'],Y))

        except TypeError:
            # 访问points['X']抛出异常,此时初始化points
            points['X'] = X
            points['Y'] = Y

            continue

    return points


def getPreRateData(df, rate, strcolsort, bolasc):

    return df[df.index < int(rate*len(df.index))].sort(columns=[strcolsort],ascending=bolasc)



def getPostRateData(df, rate,strcolsort,bolasc):

    return df[df.index > int((1-rate)*len(df.index))].sort(columns=[strcolsort],ascending=bolasc)


if '__main__' == __name__:

    main()
