county_wise = {}
for c in df1['County'].unique():
    temp = df1[df1['County'] == c]

    county_wise[c] = temp
    fig = go.Figure(
        [go.Scatter(x=temp['Date'], y=temp['Daily Mean PM2.5 Concentration'])])
    fig.update_layout(
        title="Concentration of PM2.5 in " + c,
        xaxis_title="Date",
        yaxis_title="Concentration of PM2.5",
        legend_title=c,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"))
    fig.show()

# df1['County'].unique()
