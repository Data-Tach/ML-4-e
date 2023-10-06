2+5
# Demo Comment
# print("Hello World")
print("Om Sai Ram")

# creat a variabel

x <- 2
x <- 3
x

# array of numbers
y <- c(1,2,3,4,5)
y

z <- 1:10
z

x <- y <- z
x

z <-x+y
z2 <- x*y

# List of values in the workspace 
ls()

# Delete variabel
rm(x)

rm(list = ls())

# https://cran.r-project.org/web/views/

browseURL("https://cran.r-project.org/web/views/")


install.packages("LiblineaR")

library()
search()
require("LiblineaR")
detach("package:LiblineaR",unload=TRUE)
# remove.packages("LiblineaR")

? ggplot2


data()
library(help="datasets")
? iris

str(iris)

iris

# loaddata set in workspace
data("iris")

x1 <- 1:10
x2 <- c(2,5,9)
x3 <- seq(5,50,by=5)
x4 <- scan()

Product <- read.table("D:/JYOTHIPRAKASH/desktop/MY GOLE/Data Files/1. ST Academy - Crash course and Regression files/Product.txt",header = TRUE, sep="\t")
str(Product)

Coustomer <- read.csv("D:/JYOTHIPRAKASH/desktop/MY GOLE/Data Files/1. ST Academy - Crash course and Regression files/Customer.csv",header = TRUE)
Coustomer

View(Coustomer)

# Frequency Distribution

y <- table(Coustomer$Region)
y

View(y)
# Bar-plot
barplot(y)
barplot(y[order(-y)])
# change the orientation of the barplot
barplot(y[order(y)], horiz=TRUE)
barplot(y[order(y)], horiz=TRUE, col = "red")
barplot(y[order(y)], horiz=TRUE, col = c("red", "green", "blue", "beige"))

colors()
barplot(y[order(y)], horiz=TRUE, col = c("red", "green", "blue", "beige"), border = NA, main = "Freq of Regions")

barplot(y[order(y)], horiz=TRUE, col = c("red", "green", "blue", "beige"), border = NA, main = "Freq of Regions", xlab = "Number of customers")

png(filename = "D:/JYOTHIPRAKASH/desktop/MY GOLE/Freq.png",width = 800, height = 570)
barplot(y[order(y)], horiz=TRUE, col = c("red", "green", "blue", "beige"), border = NA, main = "Freq of Regions", xlab = "Number of customers")
dev.off()

# Histogram

hist(Coustomer$Age)
hist(Coustomer$Age, breaks = 5)
hist(Coustomer$Age, breaks = c(0,40,60,100), freq=TRUE)
hist(Coustomer$Age, breaks = c(0,40,60,100), freq=FALSE, col = c("blue","green","red"), border = NA,  main = "Freq of Age Group", xlab = "Age Group")







