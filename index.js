
export default function Home() {
  return (
    <div style={{ padding: 40, fontFamily: 'Arial' }}>
      <h1>NQ Order Flow AI Dashboard</h1>

      <div style={{
        border: '1px solid #ccc',
        padding: 20,
        borderRadius: 10,
        marginTop: 20
      }}>
        <h2>Market Control</h2>
        <p>Buyers in control</p>
      </div>

      <div style={{
        border: '1px solid #ccc',
        padding: 20,
        borderRadius: 10,
        marginTop: 20
      }}>
        <h2>Large Orders</h2>
        <p>Large sell wall detected at 21251</p>
      </div>
    </div>
  )
}
