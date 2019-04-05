# Laughter-Analysis
A program that analyses call data between men and women to answer a host of questions using computer social intelligence

Data was provided by professor Alessandro Vinciarelli for the course Computer Social Intelligence

The data was reduced to a parseable dataframe which was then analysed to answer 4 distinct research questions. These questions aimed to analyse the conversations that men and women have and find out which of the sexes, laughs more, laughs longer, uses filler more, and uses filler for longer. Data analysis for these tests were done in Python3, using Pandas and Scipy APIs. The two tests used for verifying the hypotheses were the Chi Squared Test and the Student's T Test

Theory
Chi-Squared Test

Chi-squared test is used to determine whether there is a significant difference between the expected frequencies and the observed frequencies in one or more categories[1]. It is a goodness of fit test. The purpose of the test is to evaluate how likely the observations that are made would be, assuming the null hypothesis is true.

A chi-squared test can be used to attempt rejection of the null hypothesis that the data are


independent.

Student's T test

A Student's T test is used to determine if two datasets are different from each


other and how extensively

**Research Questions**

* Laughter Frequency

 Research Hypothesis: Women laugh more than men

 Null Hypothesis: Female subjects do not laugh more than men

 Test Used: Chi-Squared Test
The test is availaible as chisquare() in the scipy.stats library for python3



As evident from the results, the large value of Chi-Squared suggests a significant deviation from the expected value. With the confidence level being 0.05, it suggests that our p-value in the result falls well within 0.05, the null hypothesis can safely be rejected.

One tailed test was used due to the fact that research question stated which sex laughed more than the other, which requires analysis in only one direction for the data.

**Conclusion: Women laugh more than men**

* Filler Frequency

 Research Hypothesis: Female subjects use more filler than male subjects.

 Null Hypothesis: Female subjects do not use more filler than male subjects.

 Test used: Chi-Squared Test
The test is available as chisquare() in the scipy.stats library for python3


As evident from the results, the vale of Chi-Squared is incredibly low, with our p-value, being 0.4, which is significantly greater than 0.05, which happens to be our confidence level, therefore the null hypothesis is accepted. It can confidently be concluded that female subjects do not use more filler than their male counter parts.

One tailed test was used due to the fact that research question stated which sex used more filler than the other, which requires analysis in only one direction for the data.

Note: The degrees of freedom for Laughter and Filler frequency is 1.

**Conclusion: Women do not use more filler in conversations than men**

* Filler Duration

 Research Hypothesis: Do the Filler durations of male and female subjects differ?

 Null Hypothesis: The Filler durations of male and female subjects do not differ.

 Test Used: Student&#39;s T Test
The test is available as ttest_ind() in the scipy.stats library for python3


The arrays used to obtain these results are the filler data points for men, and the filler datapoints for women.

A two tailed test is used in this scenario, since the difference can be positive or negative, which demands that the data be analysed in both directions. This results in the confidence level being 0.05/2=0.025
Since the p-value obtained is greater than our confidence level, therefore the Null Hypothesis is accepted , filler durations for men and women do not differ.

**Conclusion: Filler durations of men and women do not differ**

* Laughter Duration

 Research Hypothesis: Do the Laughter durations of male and female subjects differ?

 Null Hypothesis: The laugter durations of male and female subjects do not differ

 Test Used: Student&#39;s T Test
The test is available as ttest_ind() in the scipy.stats library for python3


The arrays used to obtain these results are the laughter data points for men, and the laughter datapoints for women.

A two tailed test is used in this scenario, since the difference can be positive or negative, which demands that the data be analysed in both directions. This results in the confidence level being 0.05/2=0.025
Since the p-value obtained is much less than our confidence level, therefore the Null Hypothesis is rejected , laughter durations for men and women differ.

**Conclusion: Laugh durations of men and women differ**

References

--1) 2018, November "Chi-Squared Test" https://en.wikipedia.org/wiki/C


hi-squared_test

hi-squared_test

--2)144, paragraph 5D.C.Howell, "Statistical Methods for Psychology", Chapter 6, Sections 6.1, 6.3 and 6.4 (excluding subsection "Correcting for Continuity)", Cengage Learning, 2009.

--3) 185, paragraph 1, D.C.Howell, "Statistical Methods for Psychology", Chapter 7, Sections 7.1, 7.2, 7.3 (until page 186 included), 7.5 (until page 203 included), Cengage Learning, 2009.
