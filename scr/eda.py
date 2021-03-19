
def PlotPairplot(df_original,TARGET):
    

    FeaturesColumns = df_original.drop([TARGET],axis=1).columns
    pairplot_columns = st.multiselect(label="Select Features", options=FeaturesColumns)

    if st.button("Generate Plot"):
        df = df_original.copy().filter(pairplot_columns + [TARGET])
 
        if len(df.columns) > 2:
            fig = sns.pairplot(
                data=df,
                hue= TARGET,
                plot_kws={'alpha':0.8},
                # palette=sns.color_palette("RdBu_r", 7)
                )
            for i, j in zip(*np.triu_indices_from(fig.axes, 1)):
                fig.axes[i, j].set_visible(False)
            st.pyplot(fig)#,clear_figure=True)
        else:
            st.write("* Please select at least 2 columns")
