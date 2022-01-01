import quantstats as qs

qs.extend_pandas()

stock = qs. utils.download_returns("TSLA")


#print(qs.stats.sharpe(stock))


print(stock.sharpe())

stock.plot_earnings(savefig="tsla",start_balance=1000)

qs.plots.snapshot(stock, title="Tesla Performance")

qs.reports.html(stock, 'SPY', title="Tesla métricas", output='D:/Documentos/reporte.html')

