#sqlsyntax.py


def sql_select():
    sql_select= "select SUM(td.AmountOff) as totalAmtOff, ts.CouponSource from tCoupon as tc \
                 inner join tCouponDetail as td on tc.CouponID = td.CouponID    inner join \
                 tCouponSource as ts on tc.CouponSourceID = ts.CouponSourceID \
                 where td.PercentageDiscount >= 50 \
                 group by ts.CouponSource \
                 ORDER by totalAmtOff DESC"
    return sql_select;             
