# Getline 2 vs Getline 3

Getline 3 will be a radical ground-up redesign of the borrowing/lending algorithms, and will in the start run parallell with getline 2

We'll still be putting more features into getline 2

# Bitcoin fees and the missing 1 BTC

Getline has been operating without any fees on neither deposits nor withdrawals, and is now also operating with a cold/hot wallet system that is exaggerating the costs.  Getline has paid 1 BTC in fees so far, because of this 1 BTC is currently missing from the getline wallet, frequently causing the max withdrawal limit to be lower than the bitcoins that should have been available for a borrower or a lender.

We will need to start pushing the transactional costs over on the customers, and it's needed to deduct 1 BTC from the revenues and push it back into the hot wallet.

# Cold wallet vs hot wallet

Getline is currently having a cold/hot-wallet structure where all deposits comes into "cold wallet", and has to be sent from the "cold" wallet to the "hot" wallet.  Since the actual non-borrowed funds are usually quite low, the bitcoin turnover is high and the waiting time for transactions to be confirmed can be high, this also causes a liquidity problem, people want to withdraw but the hot wallet is empty.

Since the amount of bitcoins held by getline is fairly low compared to the transactional volume, the cold-wallet scheme is not so important currently, it's needed to scrap it and let all deposits be immediately available for withdrawals.

# Multi-wallet vs multi-account

Today some of the users have multiple accounts for technical reasons, i.e. one account for borrowing and one account for lending.  We'll split up "account" and "wallet", so that it's possible to have separate lending and borrowing "wallets" on one user account.  This will also allow one user to have wallets denominated in multiple currencies.

# Currencies

Getline is bitcoin-only on the deposit and withdrawal side; altcoins may be considered if the bitcoin fees gets too large - but getline is strictly a no-fiat platform.

However, we define units like "GetlineEUR", where 1 GetlineEUR is defined to be the amount of millibitcoins one would get when applying the euro rate from bitcoinaverage.com.

# Currency exchange

Sending i.e. from a bitcoin wallet to a getlineEUR wallet will be possible, but a commission will be applied.  We don't want people to be speculating on the ever-changing rates (specifically, we don't want to lose money to customers that knows more about the market than bitcoinaverage).  In the beginning we may want to keep this commission high (i.e. 1.5%).  The commission can be lowered with time.  Ideally it should be lower than 0.5%.

# NIRP

When a user is holding getlineEUR, which is backed up by bitcoins held by Getline, Getline is running a risk - if the EUR should grow or the BTC should fall, we may end up owing the customer more than the available balance.  This won't be a big problem as most funds are not held available on wallets, but borrowed between our customers.

To discourage users from holding large amounts of getlineEUR we'll apply a negative interest on the accounts bound to fiat.  It won't be big, maybe 5% APR.

This only applies to the non-invested positive balance, and only for balance held in fiat.

# Bonus for borrowers repaying the line

Currently we're taking a quite large cut of the interest paid.  We could be giving parts of this back to the borrower when the borrower successfully repays the full line.

# Auto-withdrawal for investors

Investors should have a button for withdrawing from a borrower automatically - efficiently reducing the limit whenever the borrower deposits something.

# Getline-tokens

We can sell getline tokens to our customers.  A getline token will appreciate in value based on some well-defined metrics dependent on our revenue, for instance, 5% of all interests paid can go to the token holders (leaving 25% for Getline).  (For legal reasons it's difficult to sell actual shares in the company this way, but such tokens should work out.  One of the point is to incentivize token-holders to promote getline).