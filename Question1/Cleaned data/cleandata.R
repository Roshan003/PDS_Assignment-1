raw_yield_data <- read.csv("~/Downloads/q1PDS.csv")
View (raw_yield_data)
#attach(raw_yield_data)
cleaned_yield_data <- na.omit (raw_yield_data[raw_yield_data$Frailty !="NA",])
View (cleaned_yield_data)

plot(raw_yield_data$Height,raw_yield_data$Weight,xlab="Height",ylab="Weight",main=("plot between height and weight"))
