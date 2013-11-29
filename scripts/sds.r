# load data file....
df <- read.table('~/GitHub/local/opendata/sco_diabetes/sds2012.csv', TRUE, ',')

# preview structure and contents...
str(df)
head(df,50)

# subset data (crude prevalence by typedm)
prev.t1dm <- subset(df, ind_no==2)
prev.t2dm <- subset(df, ind_no==3)

# print contents of the data frame
prev.t1dm
prev.t2dm

# create basic bar plot
barplot(prev.t1dm$measure, names.arg=prev.t1dm$hb_code)
barplot(prev.t2dm$measure, names.arg=prev.t2dm$hb_code)



