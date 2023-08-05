const listProducts = [
    {
      itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4
    },
    {
      itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10
    },
    {
      itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2
    },
    {
      itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5
    }
  ]

  import express from 'express';
  const app = express();
  app.listen(1245);

  const getItemById = (id) => {
    return listProducts.find(item => item.itemId === id);
  }


  app.get('/list_products', (req, res) => {
    res.send(listProducts);
  })

  import redis from 'redis';
  const client = redis.createClient();
  import { promisify } from 'util';

  const promisifiedSet = promisify(client.set).bind(client);
  const asyncGet = promisify(client.get).bind(client);

  const reserveStockById = (itemId, stock) => {
    promisifiedSet(`item.${itemId}`, stock);
  }

  const getStockById = async (itemId) => {
    await asyncGet(`item.${itemId}`);
  }

  app.get('/list_products/:itemId', (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById((itemId));
    if (item) {
      getStockById(itemId).then(stock => {
        item.initialAvailableQuantity = stock;
        res.send(item);
      })
    } else {
      res.status(404).send({ status:'Product not found' });
    }
  });


  app.get('/reserve_product/:itemId', (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById((itemId));
    if (!item) res.status(404).send({ status: 'Product not found' });
    if (item.initialAvailableQuantity > 0) {
      item.initialAvailableQuantity--;
      reserveStockById(itemId, item.initialAvailableQuantity);
      res.send({ "status":"Reservation confirmed", "itemId": itemId });
    } else {
      res.status(404).send({ status: 'Product not available' });
    }
  });
