library(lme4)
library(car)

packageVersion("lme4") 
packageVersion("car")  

all_metrics_df <- read.csv("/Users/xuancheng/Desktop/master github/Code-Comprehension-Cheng/all_metrics_complexity_new_categorization_summary.csv", sep=",")
#print(head(all_metrics_df)) 

lmm = lmer(formula = Line_Regression_Rate ~ Expertise + Programming_Language + Complexity + (1|Participant), data = all_metrics_df)

print(summary(lmm))

print(Anova(lmm))