# Stock Market

Stock Market is simple app for buy stocks using django and riak-kv.

## Deployment

## Contributing

```python
git clone https://github.com/adykarta/stock-market.git
cd stock-market
```

## Serve

- localhost:8000 (django)
- localhost:8098/admin/ (riak)

## Seeding

GET

```python
localhost:8000/repository/
```

## Development

Use virtualenv with python2.7

```python
git checkout -b [branch-name]
docker-compose up -d --build
docker-compose scale member=4
....code....
git add .
git commit -m [commit-message]
git push origin [branch-name]
```

Dont forget to merge request to master branch!

## Meet the Team (PDB 8)

- Muhamad Istiady Kartadibrata 1706025283
- Muthia Iftinah Parahita 1706043960
- Prissy Azzahra Ratnadwita 1706984700
- Rahmadian Tio Pratama 1706044074
