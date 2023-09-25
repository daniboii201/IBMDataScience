#load ggplot package
library(ggplot2)

#create a scatterplot of displacement (disp) and miles per gallon (mpg)

ggplot(aes(x=disp,y=mpg,),data=mtcars)+geom_point()+ggtitle("displacement vs miles per gallon") + 
  labs(x = "Displacement", y = "Miles per Gallon")

#make vs a factor
mtcars$vs <- as.factor(mtcars$vs)

#create boxplot of the distribution for v-shaped and straight Engine + add color

ggplot(aes(x=vs, y=mpg, fill = vs), data = mtcars) + 
  geom_boxplot(alpha=0.3) +
  theme(legend.position="none")

#create histogram of weight wt
ggplot(aes(x=wt),data=mtcars) + geom_histogram(binwidth=0.5)