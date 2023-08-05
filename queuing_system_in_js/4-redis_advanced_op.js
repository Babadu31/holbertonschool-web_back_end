import * as redis from 'redis';
import { createClient } from 'redis';

const client = createClient({
  host: 'localhost',
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});


const hashSet = (hashName, key, value) => {
  client.HSET(hashName, key, value, redis.print);
};


const keyHash = "HolbertonSchools";
const hashValue = {
  "Portland": "50",
  "Seattle": "80",
  "New York": "20",
  "Bogota": "20",
  "Cali": "40",
  "Paris": "2"
};

function main () {
  for (const [key, value] of Object.entries(hashValue)) {
    hashSet(keyHash, key, value);
  }
  printHash(keyHash);
}

const printHash = (hashName) => {
  client.HGETALL(hashName, (err, reply) => {
    if (err) {
      console.log(err);
    } else {
      console.log(reply);
    }
  });
}
