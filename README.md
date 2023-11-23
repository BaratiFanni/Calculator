DUE SzkriptNyelvek beadandó

Név: Barati Fanni - GDMHYR

Rövid leírás: 
  2 szám összadása,
  eredményt felugró ablakba láthatjuk, 
  számításokat egy txt fájlba menti

Modulok:
  main - függvényeket, hibakezelés, ablak értékeit, entry-t, gombokat 
  fileWrite - writeFile fájlba író függvény 
  calcMessage - különboző hibák ablakainak a messagebox-a


Függvények:
  btnClear - törli a entry értékét
  btnCl - szám gombokra, adott számot beírja az entry-be
  btnAdd - számot az entry-be elmenti fNum ként, math-nek összeadás értéket ad
  btnSub - számot az entry-be elmenti fNum ként, math-nek kivonas értéket ad
  btnMulti - számot az entry-be elmenti fNum ként, math-nek szorzas értéket ad
  btnDiv - számot az entry-be elmenti fNum ként, math-nek osztas értéket ad
  btnCalculate - ámot az entry-be elmenti sNum ként, törli a entry értékét, 
      if-elif-else elágazással kiszámolja az értéket amit a result-ba ment,
      messagebox-ba kiírja az eredményt, majd fileWrite writeFile függvénnyel fájlba menti
  failedWriteFile -  messagebox, hiba, sikeretelen fájlba írás
  valueError -  messagebox, hiba, értékbeli (pl.:5++5=)
  zeroDiv - messagebox, hiba, 0-val nem osztunk 
