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
* **flexible loan** - borrower can withdraw funds whenever (as long as he's backed by lenders with available balance) and deposit whenever, a withdrawal efficiently means to take up a loan, and a deposit is automatically considered as a payback.  A flexible loan should still have minimum repayment terms.  (Those terms may be hard coded globally in getline, or they may be set individually by each borrower).
* **credit line** - available funds for a flexible loan
* **overcommitted credit line** - if an investor has set limits for several potential borrowers and has available balance in the wallet, the credit line is said to be overcommitted.

## Amounts
* **individual** - most of the amount listed can refer to a specific borrower-lender-pair.  We may want to prefix the amounts with "individual" to emphasize this.  I.e. **individual amount owed by borrower A to lender B**.
* **total** - often we're implicitly summing together everything for a particular borrower (or a particular lender).  We may want to prefix the amounts with "total" to make it explicit.  I.e. "total amount owed by borrower A"
* **site-total** - the word "total" may also mean that we're summing over the whole site.  We should remember to be explicit on this too.
* **amount owed** - full amount the borrower should pay back.  Interest is always calculated on the amount owed.  Amount owed = principal owed + interests owed.
* **principal owed** - amount the borrower took out when borrowing the loan, that is still not paid back.  Principal owed will be unchanged if the borrower deposits less than the interests owed, and will be reduced if the borrower deposits more than the interests owed.  Principal will grow 
* **interests owed** - amount the lender will be earning if the borrower will deposit.  This is a "virtual" profit, it's not real unless the borrower actually pays back the amount owed.  Interest is also calculated on interests owed (compounded interests).  Whenever the 
* **interests earned** - interests that have been paid back.  Whenever a borrower deposits, interests paid back are considered as a real profit to the lender.  Note that the lender will still be at a loss if the borrower stops depositing.
* **individual credit line** - the minimum of funds available in the investors wallet and 



