import re


class Filter:

    def numberfilter(self,number):

        # totalCount = '已为您检索到19条近似商标'

        number = re.sub("\D", "", number)

        return number
