#coding=utf-8

import re
from collections import defaultdict
from pandas import DataFrame,concat,merge
from numpy import array,arange,concatenate
import traceback
from utils.stats import draw4,draw5,getStatsDfByGroup
import  constants

def main():
    try:

        with open(constants.DIR_LOG) as file:

            text = file.read()
            apipat = re.compile(constants.RE_API,re.S)
            content = re.findall(apipat,text)
            df = DataFrame(content,columns=['api','time'])
            df['time'] = df['time'].astype('int')
            gbdf = getStatsDfByGroup(df,'time','api',sort_key='count',ascending=False)
            print gbdf

            """
            未展示的功能:
            from uitils import getDataByRate

            print '所有api统计结果、不排序:'
            for index,row in getDataByRate(df).iterrows():
                print row

            print '所有api统计结果、按时间降序:'
            for index,row in getDataByRate(df,strcoltime='time',ascending=False).iterrows():
                print row

            print '所有api统计结果、按时间升序、 前20% ~ 24% :'
            for index,row in  getPreRateData(df,0.2,0.24,'time',True).iterrows():
                print row

            print '某个api统计结果、按时间降序、 前20% ~ 24% :'

            apidf = getApiDf(df,constants.STR_API_GET_GROUP_NAME)
            for index,row in  getDataByRate(apidf, 0.2, 0.24, 'time', False).iterrows():
                print row

            """
            points = getApiPoints(df,gbdf)
            #x,y =array([1,1,1,1,1,1]),array([2,30,32,30,100,30])
            draw5(points['X'],points['Y'])
    except Exception:
        print traceback.format_exc()


def getApiDf(df,strapi,strcolsort='',ascending=False):

    if not strapi:
        return
    res = df[df.api==strapi]
    return res if not strcolsort else res.sort(columns=[strcolsort],ascending=ascending)

def getXYs(dfapi,strcolstats,apiX):
    """Get x,y of points.

    Args:
        dfapi: a specific 'api' dateframe.
        strcolstats: an important column in the dataframe needed to be stated from which we need get the X,Y info of points.
        apiX: a contant string defined in constant.py used to mark a certain api. In other words, the same api should have the same x asix.

    Returns:
        Two array, say, X and Y. Each of these two array concatenate axis of the different apis. For
        example:

        {'X':array([1,1,1,1,2,2,2]),
         'Y':array([2.0,23.0,23.0,8.0,2.0,12.0,20.0])}

    Raises:
        TypeError: An error occurred first accessing the null array in dict.
    """

    lst =[]
    #map(lambda l: lst.append(apiX),arange(len(dfapi)))
    i = len(dfapi)
    while(i):
        lst.append(apiX)
        i -= 1
    X, Y = array(lst), array(dfapi[strcolstats])

    return X,Y

def getApiPoints(df,gbdf):
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

    lstapis = list()
    api_x = 1

    for strpath in gbdf.api:
        ##lstapis['api'].append(row)
        ##lstapis['apiX'].append(apix)
        dfapi = getApiDf(df,strpath,strcolsort='time')
        lstapis.append((dfapi,api_x,strpath))
        api_x += 1



    points = defaultdict(array)

    for tupapi in lstapis:   # 0=dfapi, 1=api_x, 2=strpath
        ###for dfapi,api_x,path in api:
        X,Y = getXYs(tupapi[0],'time',tupapi[1])
        ##X,Y = getXYs(api,'time',apiX)
        try:
        # 无异常则不是第一次循环,此时分别连接array
            points['X'] = concatenate((points['X'],X))
            points['Y'] = concatenate((points['Y'],Y))

        except TypeError:
        # 访问points['X']抛出异常,此时初始化points
            points['X'] = X
            points['Y'] = Y
            ##continue
    return points


def getDataByRate(df, rate_start=0, rate_end=100, strcolsort='', ascending=False):

    lendf = len(df.index)
    res = df[ (df.index > int( rate_start * lendf)) & (df.index < int(rate_end*lendf)) ]
    if strcolsort:
        return res.sort(columns=[strcolsort],ascending=ascending)
    return  res


if '__main__' == __name__:

    main()
