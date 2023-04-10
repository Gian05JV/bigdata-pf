chrome.runtime.onInstalled.addListener(async () => {
  // Establecer la conexión a la base de datos MongoDB
  const client = new MongoClient('mongodb://<HOST>:<PORT>', { useUnifiedTopology: true });
  await client.connect();
  const db = client.db('<DATABASE_NAME>');
  const collection = db.collection('<COLLECTION_NAME>');

  // Consultar los datos de la colección y mostrarlos en la consola del navegador
  const cursor = collection.find({});
  const data = await cursor.toArray();
  console.log(data);

  // Cerrar la conexión a la base de datos
  client.close();
});