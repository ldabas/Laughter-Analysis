import pandas as pd
import scipy.stats as stats


def laugh_frequency(data):#Method to check if women laugh more than men
    print('\nLaughter frequency:\n')

#Null Hypothesis: Women do not laugh more than men
    actual_m_laugh = laugh_count(data,'m')
    actual_f_laugh = laugh_count(data,'f')

    expected_m_laugh = total_laughter(data) * percent('m')
    expected_f_laugh = total_laughter(data) * percent('f')

    print('Male talk time: ', actual_m_laugh, '/', total_laughter(data))
    print('Female talk time: ', actual_f_laugh, '/', total_laughter(data))
    print('Expected male frequency: ', expected_m_laugh)
    print('Expected female frequency: ', expected_f_laugh)
#If women don't laugh more than men, they can only laugh less, therefore 1 tailed test should be used

    chisq, pval = stats.chisquare(f_obs=[actual_m_laugh, actual_f_laugh],
                                  f_exp=[expected_m_laugh, expected_f_laugh])
    print('Chisquared: ', chisq)
    print('pval: ', pval)



def filler_frequency(data):#16 bars no filler
    print('\nFiller frequency:\n')
#Do women use filler more than men?
    actual_m_filler = filler_filter(data,'m')
    actual_f_filler = filler_filter(data,'f')
#Null Hypothesis: women don't use more filler than men
    expected_m_filler = total_filler(data) * percent('m')
    expected_f_filler = total_filler(data) * percent('f')
#If Women don't laugh more than men, they can only laugh less, therefore 1 tailed test should be used

    print('Male talk time: ', actual_m_filler, '/', total_filler(data))
    print('Female talk time:', actual_f_filler, '/', total_filler(data))
    print('Expected male frequency: ', expected_m_filler)
    print('Expected female frequency: ', expected_f_filler)

    chisq, pval = stats.chisquare(f_obs=[actual_m_filler, actual_f_filler],
                                  f_exp=[expected_m_filler, expected_f_filler])
    print('Chisquared: ', chisq)
    print('pval: ', pval)


def laugh_period(data):
    print('\n\nLaugh Period:\n\n')
#Do men and women laugh for different durationns?
    laugh_dat = laughter(data)
#Null Hypothesis: There is no difference in laugh durations
    laugh_period_women = time_period(women(laugh_dat))
    laugh_period_men = time_period(men(laugh_dat))
#Since difference can be more than or less, than, double tailed tests should be used
    result, pval = stats.ttest_ind(a=laugh_period_men, b=laugh_period_women)
    print('Result: %.2f'% (result))
    print('P value: %.4f'%( pval))
    print('Degrees of Freedom: ', (laugh_period_men.__len__() + laugh_period_women.__len__() - 2))


def filler_period(data):
    print('\nFiller Duration:\n')
#Do men and women use filler for different periods of time?
    filler_data = filler(data)
    filler_period_women = time_period(women(filler_data))
    filler_period_men = time_period(men(filler_data))
#Null Hypothsis There is no difference in the periods of filler used betweeen men and women
    result, pval= stats.ttest_ind(a=filler_period_men, b=filler_period_women)
    print('Result: %.2f' % (result))
    print('P Value: %.4f' % (pval))
    print('Degrees of Freedom: ', (filler_period_men.__len__() + filler_period_women.__len__() - 2))
#Since difference can be more than or less than, double tailed test should be used



def main():
    data = pd.read_csv('data-part-1.csv', sep=',', header=None)#Reading in data
    filtered_data = data_cleaner(data)#Cleaning up
    global all_data
    all_data = remove_silence(data)


    print("\t\t\t\t\tHere's the data to be analysed\n\n\n\n\n\n")
    print(filtered_data)

    print('Talk Time Men\t:', talktime(filtered_data, 'm'))
    print('Talk Time Women\t:', talktime(filtered_data, 'f'))

    print('Men take up \t%2.2f\t percent of the talking time in a conversation' % (percent('m')))
    print('Women take up \t%2.2f\t percent of the talking time in a conversation' % (percent('f')))
    print('\n\n')

    print('Amount of time men use filler in a conversation:\t' + str((frequency_filler(filtered_data,'m') * 100)))
    print('Amount of time women use filler in a conversation:\t' + str((frequency_filler(filtered_data,'f') * 100)))
    print('\n\n')

    print('Percent of time men laugh in a conversation:\t' +str((frequency_laughter(filtered_data,'m') * 100)))
    print('Percent of time women laugh in a conversation:\t' +str((frequency_laughter(filtered_data,'f') * 100)))
    print('\n\n')


    ###########LAUGHTER###########
    laugh_frequency(filtered_data)
    laugh_period(filtered_data)
    ###########FILTER#############
    filler_frequency(filtered_data)
    filler_period(filtered_data)



# HELPER FUNCTIONS

def men(data):  # Returns data for men
    data = data[data[2].str.contains('M', na=False)]

    return data


def women(data):  # Returns data for women
    data = data[data[2].str.contains('F', na=False)]

    return data


def percent(s):
    if (s == 'm'):

        return talktime(all_data, 'm') / (talktime(all_data, 'm') + talktime(all_data, 'f'))
    elif (s == 'f'):

        return talktime(all_data, 'f') / (talktime(all_data, 'm') + talktime(all_data, 'f'))


def helper_count(data):  # Sums up instances of occurrences
    time_list = time_period(data)  # Did it for time, worked for everything
    sum = time_list.iloc[:, [0]].sum()
    return sum.values[0]


def data_cleaner(data):
    data_list = pd.DataFrame(data[2].str.split(' ', 1).tolist())
    data[2] = data_list[0]
    new_data = data[data[2].str.contains('laughter|filler|bc', na=False)]
    clean_data = new_data[new_data[2].str.contains('_cF|_rF|_cM|_rM', na=False)]

    return clean_data


def remove_silence(data):  # Remove all instances of silence from the dataset
    loud_data = data[~data[2].str.contains('silence', na=False)]

    return loud_data


def talktime(data, s):  # Counts number of instances of occurrence for either sex
    if (s == 'm'):

        return helper_count(men(data))

    elif (s == 'f'):

        return helper_count(women(data))


def total_laughter(data):
    return laugh_count(data, 'm') + laugh_count(data, 'f')


def total_filler(data):
    return filler_filter(data, 'm') + filler_filter(data, 'f')


def laughter(data):  # returns data only associated with laughter

    return data[data[2].str.contains('laughter', na=False)]


def filler(data):  # returns data only associated with filler
    return data[data[2].str.contains('filler', na=False)]


def time_period(data):  # returns a time period for the conversation
    time_list = data.iloc[:, [3, 4]]
    range = time_list.diff(axis=1)
    period = range.iloc[:, [1]]
    return period


###########LAUGHTER##############


def laugh_count(data, s):  # counts laughter instances for a particular sex
    if (s == 'f'):
        laughing_women = data[data[2].str.contains('laughter_cF|laughter_rF', na=False)]
        count = helper_count(laughing_women)
        return count
    elif (s == 'm'):
        laughing_men = data[data[2].str.contains('laughter_cM|laughter_rM', na=False)]
        count = helper_count(laughing_men)
        return count


def frequency_laughter(data, s):  # Returns the ratio of either sex laughing w.r.t to full laugh data
    total_laugh = laugh_count(data, 'f') + laugh_count(data, 'm')
    if (s == 'm'):
        return laugh_count(data, 'm') / total_laugh
    elif (s == 'f'):
        return laugh_count(data, 'f') / total_laugh


#############FILLER################

def filler_filter(data, s):  # counts filler instances for a particular sex
    count = 0
    if (s == 'f'):
        filler_dat = data[data[2].str.contains('filler_cF|filler_rF', na=False)]
        count = helper_count(filler_dat)
    elif (s == 'm'):
        filler_dat = data[data[2].str.contains('filler_cM|filler_rM', na=False)]
        count = helper_count(filler_dat)

    return count


def frequency_filler(data, s):  # Returns the ratio of either sex laughing w.r.t to full laugh data
    female_amount = filler_filter(data, 'f')
    male_amount = filler_filter(data, 'm')

    if (s == 'm'):
        return male_amount / total_filler(data)

    elif (s == 'f'):
        return female_amount / total_filler(data)


all_data = None#Had problems with scoping of data since code became too convoluted, so all_data is a global variable, it goes everywhere
main()#Execution