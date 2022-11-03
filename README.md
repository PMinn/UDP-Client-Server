# 網路程式設計
## Lab 5-1 UDP Client/Server
請寫一個 UDP Server 於 port 8888 接收 Client 傳來的訊息，Client 將會傳來一個整數的訊息，當 Server 收到這一個整數後印出 Client 的 IP/port 及收到的值，並將該整數值減一回傳給 Client。接著 Server 繼續等待下一個訊息。

 

請寫一個 UDP Client 程式，

(1) Client 從命令列輸入一個大於0 的整數 n 並將這一個整數傳給 Server 發起訊息傳送的動作並設定一個 timeout 時間 0.01 second；

(2) Client 在 timeout 後如果沒有收到 Server 回傳的訊息，將傳送值重設為 n 再傳給 Server;

(3) Client 在 timeout 前收到 Server 回傳的值，印出該值，如果該值為0 則結束 Client 程式，否則直接將該值再傳送給 Server。
