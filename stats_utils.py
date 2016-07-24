#!/usr/bin/env python
# encoding: utf-8
from pandas import DataFrame, concat
from numpy import array
import traceback



def statistics(df, groupby_name, stats_name):

    gdf = df.groupby(groupby_name)

    name = list()
    map(lambda line: name.append(line[0]), gdf)

    dfname = DataFrame(array(name), columns=[groupby_name])
    dfcount = DataFrame(array(gdf.count()[stats_name]), columns=[groupby_name +'count'])
    dfmax = DataFrame(array(gdf.max()[stats_name]), columns=[stats_name + 'max'])
    dfmin = DataFrame(array(gdf.min()[stats_name]), columns=[stats_name + 'min'])
#    dfavg = DataFrame(array(gdf.mean()[1]),columns=['avg'])
    dfresult = concat([dfname, dfcount, dfmax, dfmin], axis=1).sort(columns=[groupby_name +'count'], ascending=False)

    return dfresult


def draw1(x, y):

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import gaussian_kde
    from numpy import array

    # Generate fakedata
    x = array([1, 1, 1, 1, 2, 2, 2, 2])
    y = array([2, 4, 5, 2, 2, 5, 6, 8])

    # Calculate thepoint density
    xy =np.vstack([x, y])
    z =gaussian_kde(xy)(xy)
    fig, ax =plt.subplots()
    ax.scatter(x, y, c=z, s=100, edgecolor='')

    plt.show()


def draw2():

    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(0)
    n = 100000
    x = np.random.standard_normal(n)
    y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
    xmin = x.min()
    xmax = x.max()
    ymin = y.min()
    ymax = y.max()

    plt.subplots_adjust(hspace=0.5)
    plt.subplot(121)
    plt.hexbin(x, y, cmap=plt.cm.YlOrRd_r)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.title("Hexagon binning")
    cb = plt.colorbar()
    cb.set_label('counts')
    plt.subplot(122)
    plt.hexbin(x, y, bins='log', cmap=plt.cm.YlOrRd_r)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.title("With a log color scale")
    cb = plt.colorbar()
    cb.set_label('log10(N)')
    plt.show()


def draw3():

    import numpy as np
    from matplotlib import pyplot as plt

    try:
        n = 8
        X = np.arange(n) + 1
        """
        #X是1,2,3,4,5,6,7,8,柱的个数
        #numpy.random.uniform(low=0.0, high=1.0, size=None), normal
        #uniform均匀分布的随机数，normal是正态分布的随机数，0.5-1均匀分布的数，一共有n个
        """
        Y1 = np.random.uniform(0.5, 1.0, n)
        plt.figure(figsize=(len(X), len(Y1)))
        Y2 = np.random.uniform(0.5, 1.0, n)
        plt.bar(X, Y1, width=0.07, facecolor='lightskyblue', edgecolor='white')
        """
        #width:柱的宽度
        #plt.bar(X+0.35,Y2,width = 0.35,facecolor = 'yellowgreen',edgecolor = 'white')
        #水平柱状图plt.barh，属性中宽度width变成了高度height
        #打两组数据时用+
        #facecolor柱状图里填充的颜色
        #edgecolor是边框的颜色
        #想把一组数据打到下边，在数据前使用负号
        #plt.bar(X, -Y2, width=width, facecolor='#ff9999', edgecolor='white')
        #给图加text
        """
        for x, y in zip(X, Y1):
            plt.text(x +0.3, y +0.05, '%.2f' % y, ha='center', va='bottom')

        for x, y in zip(X, Y2):
            plt.text(x +0.6, y +0.05, '%.2f' % y, ha='center', va='bottom')
        plt.xlim(0, +X.max() +0.25)
        plt.ylim(0, +Y1.max() +0.25)
        plt.show()
    except Exception:
        print traceback.format_exc()


def draw4(x, y):

    from matplotlib.colors import LogNorm
    from pylab import hist2d, contour, grid, colorbar, show

    counts, ybins, xbins, image = hist2d(x, y, bins=100, norm=LogNorm())
    contour(counts, extent=[xbins.min(), xbins.max(), ybins.min(), ybins.max()], linewidths=10)
    grid(True)
    colorbar()
    show()


def draw5(x, y):

    from matplotlib.colors import LogNorm
    from pylab import hist2d, colorbar, show

    hist2d(x, y, bins=100, norm=LogNorm())
    colorbar()
    show()
