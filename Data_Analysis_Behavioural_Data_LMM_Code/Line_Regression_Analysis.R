library(lme4)
library(car)

packageVersion("lme4") 
packageVersion("car")  

all_metrics_df <- read.csv("/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/all_metrics_behavioural_data_summary.csv", sep=",")
#print(head(all_metrics_df)) 

glmm = glmer(Comprehension_Result ~ Expertise + Line_Regression_Rate + Complexity + Programming_Language + (1|Participant), data = all_metrics_df, family = binomial)

print(summary(glmm))

print(Anova(glmm))