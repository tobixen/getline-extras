(*This is work in process*)

# Definitions and concepts

Not all of those definitions may have practical implications for getline.  Some of them may still be important for the borrowers and lenders to know i.e. for taxation purposes.

## Actors
* **investor** - someone depositing money into getline and yielding credit lines to potential borrowers
* **lender** - an investor that has lended out money
* **borrower** - someone that owes money to lenders

## Loans
* **loan** - the word may be a bit overloaded, sometimes "loan" is used for "fixed loan", sometimes "loan" is used for "amount owed".  Sometimes "a loan" is used for everything a borrower owes to all the lenders, other times only about the part owed to one lender.
* **fixed loan** - the borrower and lender have agreed on fixed terms.  Funds cannot be withdrawn by the lender during the borrowing period, even if the funds are available in the borrowers wallet.  Borrower pays full interests on the loan in the borrowing period, even if he doesn't withdraw the funds.
* **flexible loan** aka **flex-loan** - borrower can withdraw funds whenever (as long as he's backed by lenders with available balance) and deposit whenever, a withdrawal efficiently means to take up a loan, and a deposit is automatically considered as a payback.  A flex-loan should still have minimum repayment terms.  (Those terms may be hard coded globally in getline, or they may be set individually by each borrower).
* **credit line** - available funds for a flex-loan
* **overcommitted credit line** - if an investor has set limits for several potential borrowers and has available balance in the wallet, the credit line is said to be overcommitted.
* **defaulted loan** - a loan that is most likely never going to be repaid.  The full amount owed is considered a loss for the lenders.  We stop calculating interests.
* **ghost repayments** - repayments on a loan that has defaulted.  Since we've already counted the full loan as a loss, every repayment should has to be considered as pure profit for the lenders.

## Amounts
* **individual** - most of the amount listed can refer to a specific borrower-lender-pair.  We may want to prefix the amounts with "individual" to emphasize this.  I.e. **individual amount owed by borrower A to lender B**.
* **total** - often we're implicitly summing together everything for a particular borrower (or a particular lender).  We may want to prefix the amounts with "total" to make it explicit.  I.e. "total amount owed by borrower A"
* **site-total** - the word "total" may also mean that we're summing over the whole site.  We should remember to be explicit on this too.
* **amount owed** - full amount the borrower should pay back.  Interest is always calculated on the amount owed.  Amount owed = principal owed + interests owed.
* **principal owed** - amount the borrower took out when borrowing the loan, that is still not paid back.  Principal owed will be unchanged if the borrower deposits less than the interests owed, and will be reduced if the borrower deposits more than the interests owed.  Principal will never grow, except when borrower withdraws more funds
* **interests owed** - amount the lender will be earning if the borrower will deposit.  This is a "virtual" profit, it's not real unless the borrower actually pays back the amount owed.  Interest is also calculated on interests owed (compounded interests).  Whenever the 
* **interests earned** - interests that have been paid back.  Whenever a borrower deposits, interests paid back are considered as a real profit to the lender.  Note that the lender will still be at a loss if the borrower stops depositing.
* **individual credit line** - the minimum of the funds available in the investors wallet and the limit set by the lender
* **hard limit** - the absolute maximum the borrower can owe to the individual lender.  Today a lender can only set the hard limit.
* **soft limit** (or maybe **wish limit**?)- the maximum principal a lender wishes to borrow to a borrower.  Can be increased or reduced any time.
* **burnout** - number of days (everything else equal) that interests can accure on a loan without hitting any of the individual hard limits.
* **available balance** - balance that can be withdrawn without taking up more loan.  Backed by real bitcoins.  Is 0 for borrowers that already has a flex-loan.
* **available for withdrawal** - available balance plus available credit line for a potential borrower

# Suggestions for getline 3

## On interest calculation

Some principles:

* All interest calculations for individual flex-loans should be done independently.  (Currently there is a dependency; there is a de-facto flow of available funds from the lender(s) with highest interest to the lenders with less interest).
* Added interest is "virtual" money; it's simply balance moved from the borrower to the lender, it does not need to be backed by bitcoins.  (Currently interests have to be backed by available balance).
* Lender and borrower should have a good overview of both the total APR and daily rate as well as the individual APRs and daily rates.
* When burnout goes to 0, we stop calculating interests.  Borrower has considered to have defaulted, and will be marked as such.  Partial repayments will be good for the reputation, but will not cause the interests to start running again.  (today, a defaulted borrower with too much debt has no incentive to do partial repayments, because everything will be eaten up by the interests).  Borrower has to pay back all he's owing before he can take out any more loans.

## Taking up a flex-loan

A person withdrawing more than his available balance from getline is indeed taking up a loan, this has to be made explicit (today people may not realize they're actually taking up a loan).  User should see the interests, lenders and total APR, and should press a button to confirm that the terms and conditions are accepted.

For getline 3.0 probably we should have the same standard "minimum payback plan" for all flex-loans.  Suggestion: each 35 days a deposit should be made, and said deposit should be minimum twice as big as the interests owed.  Failure to meet this requirement will cause reputational damage (i.e. automated warnings on the profile that he is late or has been late, possibly one can reveal some personal information to the lenders, etc).  First "friendly payment reminder" should be sent by email one week before the 35-day limit, and the next one 24 hours before the limit.  For someone that deposits (in sufficient amounts) several times a month, there will be no emails.

The individual hard limits only depends on the principal and interest rate; I suggest a loan should be going for 125 days without any deposits before it's considered defaulted.  That's equivalent to being three months late.

Rationale for 35 days: Some people pay down loans through their regular fiat salary coming in every month.  30 days is obviously too little, as some months have 31 days.  There may be other variable delays causing the payment interval to fluctate - i.e. some borrowers depends on exchanges and banking delays to buy bitcoins, if the salary comes just before the weekend, it may be some few days delay.  Congested blockchain, etc - best to give the borrower some few days extra security margin.

If a borrower is unable or unwilling to pay and some borrowers are capable to back it, the borrower can withdraw more instead of depositing, efficiently taking up a new loan with new terms.

The interest rate the borrower pays should never become bigger than what the borrower originally approved.  It can be reduced during the loan term, if more lenders joins in, or if existing lenders decides to reduce the rate.  (this may perhaps be used as an opportunity for lenders that has wished a lower soft-limit to withdraw partially or fully from the loan).

I will assume the constants "35 days", "125 days", and "installments twice the amount of interests owed" as the decided-upon configuration in the rest of this document, though the details may be adjusted.

## Taking up a bigger flex-loan

Increasing the flex-loan efficiently means replacing the existing loan with a new loan.  Algorithmically, the end-result should be the same as if the borrower had deposited the full amount owed, and then withdrawn a new and bigger loan.

This means:

* It's only possible if the total soft limit is higher than the total amount owed
* The new amount owed is considered as principal and all owed interest is now counted as interest earned
* The burnout counter is reset, and no new deposits are required for another 35 days.
* If anyone that has increased their "wanted interest rate", the new interest rate applies

It may seem counter-intuitively that lenders "earn" from borrower taking up more loans, and that the borrower gets a better reputation/burnout by taking up more loan - but it's fair, because any lender that wished to exit the loan, will get bailed out.

## Partial deposit

### Resetting the 35-day counter

The "minimum repayment plan" involves the borrower to pay twice as much as the interest owed every 35th day.  However, the devil is in the details ...

Alternative 1: When the loan is established, a repayment target is set; interests for 35 days is calculated and subtracted from the principal; within 35 days the principal should be lower or equal to this repayment target.  Whenever the repayment target is reached, the counter is reset and a new repayment target is set.  Disadvantage: the repayment plan depends on how much is deposited; the borrower may be incentivized to strategically postpone a deposit as long as possible to get a longer repayment period, borrower may also be incentivized not to deposit too much.

Alternative 2: When the loan is established, a "minimum repayment plan" is presented for the borrower, with 35 days between each installment and the maximum remaining principal calculated from the start.  Plan stays static, if the borrower does a big deposit early on, then it gives breathing room for a long time forward.  (I think we should still demand the owed interests to be paid down within 35 days, even though the borrower is months ahead of the initial repayment plan).  Disadvantages: for someone wanting to do monthly deposits, the repayment plan may look ugly since there is no fixed day of month where we expect a repayment.  more algorithmic complexity, eventually more state to the database.

### Deposit amount lower than interests owed

The deposit is distributed weighted by interest rate to all lenders.

This means the individual burnout counters will still be the same after the repayment.

The lenders are rightly intencivized to put high interest rates in order to earn high interest.  Today one is also intencivized to put high interest rates in order to get prioritized when the borrower deposits money.

The 35-day-counter for expected partial repayment will continue running, but the amount required will be less (the owed loan balance we'd require after a minimum deposit will stay the same).

### Deposit amount equal interest owed

This is just a special case of the above.  After the deposit, the burnout counter is reset, and the individual amounts owed equals the individual principals.  The 35-day-counter is still ticking though.

