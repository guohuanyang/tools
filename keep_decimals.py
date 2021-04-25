# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         keep_decimals
# Description:  
# Author:       guohuanyang
# Date:         2021/4/25
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------


from decimal import Decimal


class KeepDecimal:
    version = "1.0"

    @staticmethod
    def _gen_keep_format(keep_num):
        if keep_num == 0:
            return "0"
        return str(1/10**keep_num)

    def rounding(self, number, keep_num):
        """
        保留keep_num位小数
        :param number: 原始数据
        :param keep_num: 保留小数位数
        :return:
        """
        keep_format = self._gen_keep_format(keep_num)
        return Decimal(str(number)).quantize(Decimal(keep_format), rounding="ROUND_HALF_UP")


if __name__ == '__main__':
    obj = KeepDecimal()
    print(obj.rounding(1, 0))
    print(obj.rounding(2, 1))
    print(obj.rounding(1.345, 2))
    print(obj.rounding(2.35, 1))
