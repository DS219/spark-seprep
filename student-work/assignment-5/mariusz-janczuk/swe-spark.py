class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        splitted_dates = []
        splitted_dates = list(date.split("-"))
        print(splitted_dates)
        integered_splt_date = []

        for i in range(len(splitted_dates)):
            integered_splt_date.append(int(splitted_dates[i]))

        bin_int_splt_date = []
        for i in range(len(splitted_dates)):
            bin_int_splt_date.append(bin(integered_splt_date[i])[2:])  # now i have binaries in a list
        bin_final_string = ""

        for i in range(len(bin_int_splt_date)):
            bin_final_string += str(bin_int_splt_date[i])
            if i <= len(bin_int_splt_date)-2:
                bin_final_string += "-"

        return bin_final_string #should return a date 
        
if __name__ == "__main__":
    s = Solution()
    print(s.convertDateToBinary("2024-02-22"))