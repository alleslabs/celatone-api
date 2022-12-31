# Cosmos Registry API

This repository contains the implementation of an API wrapper around the Alles Labs' [Cosmos Registry](https://github.com/alleslabs/cosmos-registry).

## Routes

### Global

#### Entities

| Endpoint     | Description                                                       | Path                    | Response |
| ------------ | ----------------------------------------------------------------- | ----------------------- | -------- |
| Entity list  | Returns the list of all entites in the registrar                  | `/entities`             | []Entity |
| Entity by ID | Returns a single entity record that matches the query ENTITY_SLUG | `/entity/<ENTITY_SLUG>` | Entity   |

### By Chain and Network

#### Projects

| Endpoint      | Description                                                                                            | Path                                      | Response  |
| ------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------- | --------- |
| Project list  | Returns the list of all projects in the registrar for the given CHAIN and NETWORK pair                 | `/<CHAIN>/<NETWORK>/projects`             | []Project |
| Project by ID | Returns a single project record for the given CHAIN and NETWORK pair that matches the query PROJECT_ID | `/<CHAIN>/<NETWORK>/project/<PROJECT_ID>` | Project   |

### Contracts

| Endpoint      | Description                                                                                                   | Path                                             | Response   |
| ------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------- |
| Project list  | Returns the list of all contracts in the registrar for the given CHAIN and NETWORK pair                       | `/<CHAIN>/<NETWORK>/contracts`                   | []Contract |
| Project by ID | Returns a single contract record for the given CHAIN and NETWORK pair that matches the query CONTRACT_ADDRESS | `/<CHAIN>/<NETWORK>/contract/<CONTRACT_ADDRESS>` | Contract   |

### Codes

| Endpoint      | Description                                                                                      | Path                                | Response |
| ------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------- | -------- |
| Project list  | Returns the list of all codes in the registrar for the given CHAIN and NETWORK pair              | `/<CHAIN>/<NETWORK>/codes`          | []Code   |
| Project by ID | Returns a single code record for the given CHAIN and NETWORK pair that matches the query CODE_ID | `/<CHAIN>/<NETWORK>/code/<CODE_ID>` | Code     |

### Accounts

| Endpoint      | Description                                                                                                 | Path                                           | Response  |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------- |
| Project list  | Returns the list of all accounts in the registrar for the given CHAIN and NETWORK pair                      | `/<CHAIN>/<NETWORK>/accounts`                  | []Account |
| Project by ID | Returns a single account record for the given CHAIN and NETWORK pair that matches the query ACCOUNT_ADDRESS | `/<CHAIN>/<NETWORK>/account/<ACCOUNT_ADDRESS>` | Account   |

### Assets

| Endpoint        | Description                                                                                                                       | Path                                           | Response |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------- |
| Asset list      | Returns the list of all assets in the registrar for the given CHAIN and NETWORK pair                                              | `/<CHAIN>/<NETWORK>/assets`                    | []Asset  |
| Asset by entity | Returns the list of asset records for the given CHAIN and NETWORK pair that matches the entity project ENTITY_SLUG                | `/<CHAIN>/<NETWORK>/assets/slug/<ENTITY_SLUG>` | []Asset  |
| Asset by type   | Returns the list of all assets for the given CHAIN and NETWORK pair that matches the query asset type (either "native" or "cw20") | `/<CHAIN>/<NETWORK>/assets/type/<ASSET_TYPE>`  | []Asset  |
| Asset by ID     | Returns a single asset record for the given CHAIN and NETWORK pair that matches the query ID                                      | `/<CHAIN>/<NETWORK>/asset/<ASSET_ID>`          | Asset    |

### Balances

| Endpoint         | Description                                                                                          | Path                                                       | Response  |
| ---------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------- |
| Balances list    | Returns the list of all non-zero balance records for an account for the given CHAIN and NETWORK pair | `/<CHAIN>/<NETWORK>/balances/<ACCOUNT_ADDRESS>`            | []Balance |
| Balance by asset | Returns a balance record for an account for the given CHAIN and NETWORK pair                         | `/<CHAIN>/<NETWORK>/balances/<ACCOUNT_ADDRESS>/<ASSET_ID>` | Balance   |
