# Wumpus World
## 1. ailogic/mainlogic.py
- Hàm main trong này sẽ được chảy mõi lần cập nhật (nằm trong vòng while), truyền vào 2 tham số là gamemap và gamecontrol
- Hiện giờ đang chạy 60fps nên khá nhanh, có thể giảm lại bằng cách sử dụng time.sleep(1)

## 2. status
- BREEZE
- STENCH
- PIT
- WUMPUS
- AGENT
- GOLD
- BLANK

## 2. gamemap
- `has_status(self, row, col, status)`: kiểm tra có status nào đó không
- `ví dụ như: gamemap.has_status(1, 5, BREEZE) trả về True/False`

## 3. directions
- LEFT
- RIGHT
- TOP
- BOTTOM

## 4. gamecontrol
- `move(self, direction)`: di chuyển agent theo hướng cố định, trả về một mảng 2 chiều chứa vị trí hiện tại của agent.
- `row, col = gamecontrol.move(LEFT)`
- `if (gamemap.has_status(row, col, PIT)): print("Lose")`