# Azalea Rohr 

My favorite programing language is R. I know that some people say that it is not a real programming language, but I like the stats part of DS more then the coding part, which is why I think I like R so much. I have had the best professors when I was learning R and the material has interested me the most.

## Example code 
x = 8.2 
sdx = 13.2 
y= 45.1
sdy = 5.6 
rxy = 0.8754 
n = 24 

B1 = rxy*(sdy/sdx)
round(B1,2) #0.37 
B0 = y - (B1*x) #here is for the y intersept 
round(B0,2) #42.05

var_ygivex <- SSE / (n - 2)
round(var_ygivex,2) #7.66

#q9
SSM <- (rxy^2) * SST
round(SSM,2) #552.74

SSE = (sdy^2)*(n-1)*(1-rxy^2)
round(SSE,2) #168.54

SST <- (n - 1) * (sdy^2)
round(SST,2) 

### Code Explanation

Above is simple code of how to find the slope, y intercept, varience of y given x, SSM, SSE, and SST for when x = 8.2, y = 45.1, the correlation coefficient between X and Y is 0.8754, and sample size is 24. 
Usually in R you will have a data set and then define each of these varbles through this data set, but when you hard code those varible values, you are able to simpley copy and paste this code into R studio and
run it. 
