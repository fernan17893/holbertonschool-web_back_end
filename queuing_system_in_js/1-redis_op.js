import redis from 'redis';

const client = redis.createClient();

client.on("connect", () => {
    console.log("Redis client connected");
});

client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, res) => {
        if (err) throw err;
        console.log(res);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
