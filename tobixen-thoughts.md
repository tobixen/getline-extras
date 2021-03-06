(*This is work in process*)

# Definitions and concepts

Not all of those definitions may have practical implications for getline.  Some of them may still be important for the borrowers and lenders to know i.e. for taxation purposes.

## Actors
* **investor** - someone depositing money into getline and yielding credit lines to potential borrowers
* **lender** - an investor that has lended out money
* **borrower** - someone that owes money to lenders
* **reputation** - getline 2 doesn't have any kind of reputational scoring system, and probably getline 3 also shouldn't have it.  In this document, "reputation" is used either to describe factual information displayed about a user (automated warnings if the user has been late, are late on other platforms, graphs displaying performance, etc), user comments and the impression potential investors have on a potential borrower.

## Loans
* **loan** - the word may be a bit overloaded, sometimes "loan" is used for "fixed loan", sometimes "loan" is used for "amount owed".  Sometimes "a loan" is used for everything a borrower owes to all the lenders, other times only about the part owed to one lender.
* **fixed loan** - the borrower and lender have agreed on fixed terms.  Funds cannot be withdrawn by the lender during the borrowing period, even if the funds are available in the borrowers wallet.  Borrower pays full interests on the loan in the borrowing period, even if he doesn't withdraw the funds.
* **flexible loan** aka **flex-loan** - borrower can withdraw funds whenever (as long as he's backed by lenders with available balance) and deposit whenever, a withdrawal efficiently means to take up a loan, and a deposit is automatically considered as a payback.  A flex-loan should still have minimum repayment terms.  (Those terms may be hard coded globally in getline, or they may be set individually by each borrower).
* **credit line** - available funds for a flex-loan.
* **overcommitted credit line** - if an investor has set limits for several potential borrowers and has available balance in the wallet, the credit line is said to be overcommitted.
* **defaulted loan** - a loan that is most likely never going to be repaid.  The full amount owed is considered a loss for the lenders.  We stop calculating interests.
* **ghost repayments** - repayments on a loan that has defaulted.  Since we've already counted the full loan as a loss, every repayment should has to be considered as pure profit for the lenders.

## Amounts
* **individual** - most of the amount listed can refer to a specific borrower-lender-pair.  We may want to prefix the amounts with "individual" to emphasize this.  I.e. **individual amount owed by borrower A to lender B**.
* **total** - often we're implicitly summing together everything for a particular borrower (or a particular lender).  We may want to prefix the amounts with "total" to make it explicit.  I.e. "total amount owed by borrower A"
* **site-total** - the word "total" may also mean that we're summing over the whole site.  We should remember to be explicit on this too.
* **amount owed** - full amount the borrower should pay back.  Interest is always calculated on the amount owed.  Amount owed = principal owed + interests owed.
* **principal owed** - amount the borrower took out when borrowing the loan, that is still not paid back.  Principal owed will be unchanged if the borrower deposits less than the interests owed, and will be reduced if the borrower deposits more than the interests owed.  Principal will never grow, except when borrower withdraws more funds
* **interests owed** - amount the lender will be earning if the borrower will deposit.  This is a "virtual" profit, it's not real unless the borrower actually pays back the amount owed.  Interest is also calculated on interests owed (compounded interests).
* **interests earned** - interests that have been paid back.  Whenever a borrower deposits, interests paid back are considered as a real profit to the lender.  Note that the lender will still be at a loss if the borrower stops depositing.  In getline 2.0 the lower-interest lenders actually earns profit every day, this is deducted from the available balance of the higher-interest lender(s)
* **site fees owed** - part of the interests owed by a borrower that goes as fees to getline.  Note that as of getline 2.0, site fees are taken from the lenders available funds
* **site fees paid** - actual getline profit, probably generated when the borrower deposits money in getline 3.0, generated daily in getline 2.0.
* **individual credit line** - the minimum of the funds available in the investors wallet and the limit set by the lender
* **hard limit** - the absolute maximum the borrower can owe to the individual lender.  Today a lender can only set the hard limit.
* **soft limit** (or maybe **wish limit**?)- the maximum principal a lender wishes to borrow to a borrower.  Can be increased or reduced any time.
* **burnout** - number of days (everything else equal) that interests can accure on a loan without hitting any of the individual hard limits.  Note that the proposed algorithm for getline 3.0 is very different from getline 2.0; in getline 2.0 the burnout depends on available credit line and can fluctuate wildly; in the new proposed algorithm it will be a real countdown, only affected by the borrower either depositing or withdrawing.
* **available balance** - balance that can be withdrawn without taking up more loan.  Backed by real bitcoins.  Is 0 for borrowers that already has a flex-loan.
* **available for withdrawal** - available balance plus available credit line for a potential borrower

# Suggestions for getline 3

## On interest calculation

Some principles:

* All interest calculations for individual flex-loans should be done independently.  (Currently there is a dependency; there is a de-facto flow of available funds from the lender(s) with highest interest to the lenders with less interest).
* Added interest is "virtual" money; it's simply balance moved from the borrower to the lender, it does not need to be backed by bitcoins.  (Currently interests have to be backed by available balance).
* Lender and borrower should have a good overview of both the total APR and daily rate as well as the individual APRs and daily rates.
* When burnout goes to 0, we stop calculating interests.  Borrower has considered to have defaulted, and will be marked as such.  Partial repayments will be good for the reputation, but will not cause the interests to start running again.  (today, a defaulted borrower with too much debt has no incentive to do partial repayments, because everything will be eaten up by the interests).  Borrower has to pay back all he's owing before he can take out any more loans.

## Borrower requesting a credit line

I have no strong opinions on how this should work.

In getline 2.0 a request for a credit line is not affecting the business logic anyhow.  The request is just static variables that are presented to the lenders.

In getline 3.0, a potential borrower should be able to pay a bit for the unused credit line.  I think the borrower should be presented with a menu where the borrower can tell how big credit line he's willing to pay for, and how much interest he's willing to pay for the credit line itself.  Probably the user interface should give a good recommendation; 0.001% pr day, equivalent with 3.7% APR, sounds fair.

## Borrower taking up a flex-loan

A person withdrawing more than his available balance from getline is indeed taking up a loan, this has to be made explicit (today people may not realize they're actually taking up a loan).  User should see the interests, lenders and total APR, and should press a button to confirm that the terms and conditions are accepted.

For getline 3.0 probably we should have the same standard "minimum payback plan" for all flex-loans.  Suggestion: each 35 days a deposit should be made, and said deposit should be minimum twice as big as the interests owed.  Failure to meet this requirement will cause reputational damage (i.e. automated warnings on the profile that he is late or has been late, possibly one can reveal some personal information to the lenders, etc).  First "friendly payment reminder" should be sent by email one week before the 35-day limit, and the next one 24 hours before the limit.  For someone that deposits (in sufficient amounts) several times a month, there will be no emails.

The individual hard limits only depends on the principal and interest rate; I suggest a loan should be going for 125 days without any deposits before it's considered defaulted.  That's equivalent to being three months late.

Rationale for 35 days: Some people pay down loans through their regular fiat salary coming in every month.  30 days is obviously too little, as some months have 31 days.  There may be other variable delays causing the payment interval to fluctate - i.e. some borrowers depends on exchanges and banking delays to buy bitcoins, if the salary comes just before the weekend, it may be some few days delay.  Congested blockchain, etc - best to give the borrower some few days extra security margin.

If a borrower is unable or unwilling to pay and some borrowers are capable and willing to back it, the borrower can withdraw more instead of depositing, efficiently taking up a new loan with new terms.

The interest rate the borrower pays should never become bigger than what the borrower originally approved.  It can be reduced during the loan term, if more lenders joins in, or if existing lenders decides to reduce the rate.  (this may perhaps be used as an opportunity for lenders that has wished a lower soft-limit to withdraw partially or fully from the loan).

I will assume the constants "35 days", "125 days", and "installments twice the amount of interests owed" as the decided-upon configuration in the rest of this document, though the details may be adjusted.

## Borrower taking up a bigger flex-loan

Increasing the flex-loan efficiently means replacing the existing loan with a new loan.  Algorithmically, the end-result should be the same as if the borrower had deposited the full amount owed, and then withdrawn a new and bigger loan.

This means:

* It's only possible if the total soft limit is higher than the total amount owed
* The new amount owed is considered as principal and all owed interest is now counted as interest earned
* The burnout counter is reset, and no new deposits are required for another 35 days.
* If anyone that has increased their "wanted interest rate", the new interest rate applies

It may seem counter-intuitively that lenders "earn" from borrower taking up more loans, and that the borrower gets a better reputation/burnout by taking up more loan - but it's fair, because any lender that wished to exit the loan, will get bailed out.  Also, only a good borrower (or a very clever scammer) will have a good available credit line allowing more loan to be taken out.

## Borrower partially depositing

### Resetting the 35-day counter

The "minimum repayment plan" involves the borrower to pay twice as much as the interest owed every 35th day.  However, the devil is in the details ...

Alternative 1: When the loan is established, a repayment target is set; interests for 35 days is calculated and subtracted from the principal; within 35 days the principal should be lower or equal to this repayment target.  Whenever the repayment target is reached, the counter is reset and a new repayment target is set.  Disadvantage: the repayment plan depends on how much is deposited; the borrower may be incentivized to strategically postpone a deposit as long as possible to get a longer repayment period, borrower may also be incentivized not to deposit too much.

Alternative 2: When the loan is established, a "minimum repayment plan" is presented for the borrower, with 35 days between each installment and the maximum remaining principal calculated from the start.  Plan stays static, if the borrower does a big deposit early on, then it gives breathing room for a long time forward.  (I think we should still demand the owed interests to be paid down within 35 days, even though the borrower is months ahead of the initial repayment plan).  Disadvantages: for someone wanting to do monthly deposits, the repayment plan may look ugly since there is no fixed day of month where we expect a repayment.  This alternative involves more algorithmic complexity, and perhaps more state to the database.

### Deposit amount lower than interests owed

The deposit is distributed weighted by interest rate to all lenders.

This means all the individual burnout counters will be equal after the repayment.

The lenders are rightly intencivized to put high interest rates in order to earn high interest.  Today one is also intencivized to put high interest rates in order to get prioritized when the borrower deposits money.

The 35-day-counter for expected partial repayment will continue running, but the amount required will be less (the owed loan balance we'd require after a minimum deposit will stay the same).

### Deposit amount equal interest owed

This is just a special case of the above.  After the deposit, the burnout counter is reset, and the individual amounts owed equals the individual principals.  The 35-day-counter is still ticking though.

### Deposit amount is higher than interest owed

(Work in progress)

#### Honoring reduced soft rates

When the interest owed is paid down, the next priority is to bail out lenders that wants to get out of the loan (or who wants to reduce their stake).

Whom to prioritize?  If many lenders wants to get out from a loan, it means they have some doubts in the borrower.  Borrower may be in financial troubles.  It's paramount that we reduce the burden as much as possible.  It would be in the borrowers best interest to start by getting rid of the highest-interest-lenders (and this may also incentivize the borrower to pay back as much and as soon as possible), but at the other hand we also want to intencivize lenders to give lower rate in such case - not the highest possible rate.  Suggestion for a compromise: split the (remaining) deposit in two, 50% of the deposit will be used to bail out the lenders with lowest interest rate, and 50% of the deposit will be used to bail out the lendes with highest interest rate.

#### Bailing out the highest-interest lenders

Whatever is left is used on bailing out the highest-interest lenders (in the borrowers interest to get rid of those)

## Calculation of interest on an unused credit line

The interest used when counting is always the rate given by the potential borrower, investor has no say on it.  The interest given is to be seen as an incentive for the investor to keep available funds in the getline wallet and to give out lines to potential borrowers, even when those potential borrowers don't need to take up a loan.

If a potential borrower has available funds, the interests are paid immediately daily to the investor, and is counted as profit for the investor.  If there is no available funds, then ... TODO: what?  Consider it as a new loan taken?  And count interests on said loan?

For the interest to count, the credit line must have been available for a full 24 hours (otherwise an attacker may easily set up a script yielding a relatively risk-free credit line just before midnight and removing it again some few seconds later).  Similarly, we may need protection against the potential borrower temporarily reducing the interest rate just before midnight (though, probably less of a problem as the reputational damage can be real).

An investor can earn interest multiple times on overcommitted credit lines.  If an investor gives a credit line to a sufficient amount of potential borrowers and ensures there always is available funds in the wallet, it should even be possible to earn more money on the credit line than on the lendings.  Consider that the the investor is taking a risk by giving out a credit line; A scammer may run away with the funds at once, a legitimate borrower may decide he doesn't need the line.  Overcommitment is good, a massive amount of investors heavily overcommiting their credit lines and doing their best to keep available balance in their wallets is the only way we can give potential borrowers a predictable credit line.

If a borrower has more credit lines than what he's willing to pay for, the credit lines with lowest interest will be prioritized.

If multiple credit lines have same interest rate, the less overcommitted line will be prioritized.

Last resort; if there are more credit lines with same interest rate and same overcommitment rate, the interests paid are split on the remaining credit lines.

## New lender joining in, outcompeting existing lenders

Say, a new lender wants to joins the party and puts a lower interest rate on a borrower than what the existing lenders are getting out from the flex-loan.  The new lender should instantly be included in the flex-loan.  This is how it works in getline 2.0, and it should continue working like that in getline 3.0.

If comparing this to the borrower immediately depositing the credit line offered by the new borrower and then immediately withdrawing the same money, keeping the balance intact - there are some notable differences:
* We may consider to honor wishes from other lenders on increased interest rate or reduced wish-limit, but eventually the new APR should not grow.
* Obviously, depositing and then immediately withdrawing the same amount may fail due to lenders that have reduced their wish-limits; a new lender joining the party should not fail.
* The 35-day countdown should not be affected (but if the new lender contributes with significant funds, the borrower may reset the counter by increasing the loan)
* The burnout should (probably) not be affected (but if the new lender contributes with significant funds, the borrower may reset the counter by increasing the loan)
