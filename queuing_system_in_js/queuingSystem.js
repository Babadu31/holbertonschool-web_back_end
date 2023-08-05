const redis = require("redis");
const { promisify } = require("util");

const client = redis.createClient();

// Promisify the Redis commands for easier use with async/await
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Connect to the Redis server
client.on("connect", () => {
  console.log("Connected to Redis server");
});

// Set the value "School" for the key "Holberton"
async function setSchoolValue() {
  try {
    const response = await setAsync("Holberton", "School");
    console.log(response); // Should print "OK"
  } catch (error) {
    console.error("Error setting value:", error);
  } finally {
    client.quit(); // Quit the Redis client
  }
}

// Get the value for the key "Holberton"
async function getSchoolValue() {
  try {
    const response = await getAsync("Holberton");
    console.log(response); // Should print "School"
  } catch (error) {
    console.error("Error getting value:", error);
  } finally {
    client.quit(); // Quit the Redis client
  }
}

// Uncomment the following line to set the value "School" for the key "Holberton"
// setSchoolValue();

// Uncomment the following line to get the value for the key "Holberton"
// getSchoolValue();
