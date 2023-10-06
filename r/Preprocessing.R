df <- read.csv("D:/JYOTHIPRAKASH/desktop/MY GOLE/Data Files/1. ST Academy - Crash course and Regression files/House_Price.csv",header = TRUE)

str(df)

# EDD
summary(df)

hist(df$crime_rate)
pairs(~price+crime_rate+n_hot_rooms+rainfall, data = df)
barplot(table(df$airport))
barplot(table(df$waterbody))
barplot(table(df$bus_ter))

# Observation :
# 1) n_hos_rooms and rainfall has outlines
# 2) n_hos_beds has missing values
# 3) crime_rate is having some functional relation with price
# 4) bus_ter is a useless variable

# outline Removal 
quantile(df$n_hot_rooms,0.99)
uv = 3*quantile(df$n_hot_rooms,0.99)
uv
df$n_hot_rooms[df$n_hot_rooms>uv] <- uv
summary(df$n_hot_rooms)

lv = 0.3*quantile(df$rainfall,0.01)
lv
df$rainfall[df$rainfall<lv] <- lv
summary(df$rainfall)

# Missing values handing
mean(df$n_hos_beds)
mean(df$n_hos_beds, na.rm = TRUE)
which(is.na(df$n_hos_beds))
df$n_hos_beds[is.na(df$n_hos_beds)] <- mean(df$n_hos_beds, na.rm = TRUE)
summary(df$n_hos_beds)


# crime_rate is having some functional relation with price
pairs(~price+crime_rate, data = df)
plot(df$crime_rate, df$price)
df$crime_rate = log(1+df$crime_rate)


# transform the 4 distance variable into one distance variable 
df$avg_dist = (df$dist1+df$dist2+df$dist3+df$dist4)/4
df2 <- df[,-7:-10]
df <- df2
rm(df2)


# remove the bus_terminal variable
df2 <- df[,-14]
df <- df2
rm(df2)

# Dummy variable for all the categorical values

install.packages("dummies")
df <- dummy.data.frame(df)
df <- df[,-9]
df <- df[-14]

# get the correlation between the two variables

cor(df)
round(cor(df), 2)
df <- df[,-16]
df





