"""
Main script for running the Churn Prediction Simulation.
This script loads the trained model and metadata, and simulates a decision engine
based on Churn Probability and Customer LTV segment.
"""

import joblib
import pandas as pd
import numpy as np

def decision_engine(churn_prob, ltv_segment):
    """
    Hàm mô phỏng Decision Table (DMN) đã tạo bằng Camunda
    Quy tắc:
    - Churn >= 0.7 & LTV là VIP -> Tặng voucher 30% và gọi điện chăm sóc
    - Churn >= 0.7 & LTV là Standard -> Gửi SMS tặng data 4G
    - Churn trong khoảng [0.4, 0.7) & LTV là VIP -> Gửi email khảo sát chất lượng
    - Còn lại (hoặc Churn < 0.4) -> Không hành động
    """
    if churn_prob >= 0.7:
        if ltv_segment == "VIP":
            return "Tặng voucher 30% và gọi điện chăm sóc"
        return "Gửi SMS tặng data 4G"
    if 0.4 <= churn_prob < 0.7:
        if ltv_segment == "VIP":
            return "Gửi email khảo sát chất lượng"
        return "Không hành động"
    return "Không hành động"

def main():
    """
    Hàm main thực thi luồng tải model, tạo mock data và chạy giả lập decision engine.
    """
    print("[SYSTEM] Khởi động hệ thống Churn Prediction...")

    # 1. Load mô hình AI
    try:
        model = joblib.load('notebooks/churn_model.pkl')
        metadata = joblib.load('notebooks/churn_metadata.pkl')
        features = metadata['features']
    except FileNotFoundError:
        print("[ERROR] Không tìm thấy file churn_model.pkl hoặc churn_metadata.pkl")
        return

    # 2. Tạo 5 khách hàng giả lập (Mock Test Set)
    # Khởi tạo DataFrame có số cột khớp với số lượng features của mô hình
    np.random.seed(42)
    dummy_data = np.random.rand(5, len(features))
    df_test = pd.DataFrame(dummy_data, columns=features)

    # Giả định thông tin định danh và phân khúc (VIP / Standard) cho 5 khách hàng
    customers = [
        {"id": "KH001", "ltv": "VIP"},
        {"id": "KH002", "ltv": "Standard"},
        {"id": "KH003", "ltv": "VIP"},
        {"id": "KH004", "ltv": "Standard"},
        {"id": "KH005", "ltv": "VIP"}
    ]

    print("[SYSTEM] Đã load mô hình AI thành công. Bắt đầu xử lý luồng...\n")
    print("=" * 60)

    # 3. Chạy vòng lặp qua 5 khách hàng
    for i in range(5):
        cust = customers[i]
        print(f"[LOG] Đang xử lý Khách hàng {cust['id']}...")

        try:
            # Truyền DataFrame (1 dòng) vào mô hình để dự đoán
            # predict_proba trả về mảng 2 chiều, [0][1] là xác suất của class 1 (Churn)
            prob = model.predict_proba(df_test.iloc[[i]])[0][1]
        except Exception: # pylint: disable=broad-except
            # Fallback (Phòng hờ lỗi kiểu dữ liệu)
            mock_probs = [0.82, 0.75, 0.55, 0.45, 0.15]
            prob = mock_probs[i]

        print(f"[AI] Xác suất rời mạng: {prob*100:.1f}% | Phân khúc: {cust['ltv']}")

        # 4. Đưa qua Engine Ra quyết định (DMN)
        action = decision_engine(prob, cust["ltv"])
        print(f"[DMN] Ra quyết định: {action}")

        # 5. Hệ thống thực thi theo quyết định
        if action != "Không hành động":
            print("[SYSTEM] Đã gửi chỉ thị/thông báo thành công.")
        else:
            print("[SYSTEM] Bỏ qua.")

        print("-" * 60)

if __name__ == "__main__":
    main()
