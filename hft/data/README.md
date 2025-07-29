# Stock Exchange Trade Data

Sample orderbook and tradebook data from a stock exchange for one trading day. Contains 5 randomly selected stocks with masked identifiers for academic learning purposes.

## File Structure

```
orders_1.csv, trades_1.csv    # Stock 1 data
orders_2.csv, trades_2.csv    # Stock 2 data
orders_3.csv, trades_3.csv    # Stock 3 data
orders_4.csv, trades_4.csv    # Stock 4 data
orders_5.csv, trades_5.csv    # Stock 5 data
```

Each `orders_i.csv` contains the orderbook for stock i, and `trades_i.csv` contains the corresponding executed trades.

## Data Schema

### Orderbook (`orders_i.csv`)

| Field | Description | Values/Notes |
|-------|-------------|--------------|
| Record Indicator | Trading session type | `PO` = Call auction, `RM` = Continuous trading |
| Order Number | Unique order identifier | Masked from real data |
| Transaction Time | Order timestamp | HH:MM:SS format |
| Buy/Sell Indicator | Order side | `B` = Buy, `S` = Sell |
| Activity Type | Order action | `1` = Entry, `3` = Cancel, `4` = Modify |
| Volume Disclosed | Visible order quantity | For iceberg orders |
| Volume Original | Total order quantity | Full order size |
| Limit Price | Order price limit | Price per share |
| Trigger Price | Stop loss trigger | Populated for stop orders only |
| Market Order Flag | Market order indicator | Y for market order |
| Stop Loss Flag | Stop loss order indicator | Y for stoploss order |
| IO Flag | Immediate or Cancel flag | Y for IOC orders |

### Tradebook (`trades_i.csv`)

| Field | Description | Notes |
|-------|-------------|-------|
| Record Indicator | Trading session type | `PO` = Call auction, `RM` = Continuous trading |
| Trade Time | Execution timestamp | HH:MM:SS format |
| Trade Price | Execution price | Price per share |
| Trade Quantity | Number of shares traded | Volume executed |
| Buy Order Number | Buyer's order ID | References orderbook |
| Sell Order Number | Seller's order ID | References orderbook |

## Data Relationships

- Each tradebook file corresponds to its matching orderbook file (same stock)
- Buy/Sell Order Numbers in trades reference Order Numbers in the orderbook
- All identifiers (order IDs, stock names) are masked from original exchange data

## Usage

This dataset is intended for academic learning in market microstructure and data analysis.
