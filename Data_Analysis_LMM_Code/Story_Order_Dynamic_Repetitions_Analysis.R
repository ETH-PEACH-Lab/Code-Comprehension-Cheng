library(lme4)
library(car)

packageVersion("lme4") 
packageVersion("car")  

all_metrics_df <- read.csv("/Users/xuancheng/Desktop/Master Thesis /Thesis_Data_Code/all_metrics_summary.csv", sep=",")
#print(head(all_metrics_df)) 

lmm = lmer(formula = Story_Order_Dynamic_Repetitions ~ Expertise + Programming_Language + (1|Participant), data = all_metrics_df)

print(summary(lmm))

print(Anova(lmm))