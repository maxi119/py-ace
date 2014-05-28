
透過 cython 將 script 轉換成 c 模組 
加快執行速度, 使源始碼更難破解.....

轉換過程會有一些之 error 被檢查出來
變數未定義, 語法不正確等...
因為要先轉換為 C，所以一些不常跑到的程式碼
像一些測試用的，就不能被轉換
另外一些使用到內建的變數如 __file__ 的檔案也不適合轉換
列在 keep_source 的項目裡就會保留避免轉換成 c 模組

tab 和 空白在同一個檔案也不能混用
如果用混用到請將少數的部份修正

一些如 config 的檔案不希望在解壓時覆蓋到原本修改好的設定
設定在 exclude 裡面

因為使用 c 語言而且使用了最佳化的選項
因此 20 個檔案大約需要 5 分鐘轉換的時間

cython 可以混合使用 python 語法和 cython 語法
即使不使用 cython 的語法也可以
使用 cython 語法可以加速運算

另外 cython 可以控制 gil lock 
可以在安全的範圍內釋放 gli
	with nogil:
		'  do something '

使用 cython 執行速度可以和 c 一樣快
http://blog.csdn.net/gzlaiyonghao/article/details/4561611


1.	在 Windows 中如果有安裝 MSVC 2008 以外的版本
	要先準備好開發環境
	例如：

	"%VS100COMNTOOLS%vsvars32.bat"
	set DISTUTILS_USE_SDK=1
	set MSSdk=1

2.	執行 python cython_setup.py build_ext --inplace
	沒有錯誤的話會產生一個 zip 

