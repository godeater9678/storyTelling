from sqlalchemy import Column, BigInteger, DECIMAL, Date, Time, DateTime, Integer
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from com.switchwon.dao.db import get_database_connection_exchange

# 데이터베이스 연결 설정 (MySQL의 경우)
engine = get_database_connection_exchange()
Base = declarative_base()


# WalletBlockTransaction 모델 정의
class wallet_block_transaction_entity(Base):
    __tablename__ = 'WalletBlockTransaction'

    id = Column(Integer, primary_key=True, comment='식별값')
    walletId = Column(BigInteger, nullable=False, comment='userWallet id')
    transactionType = Column(VARCHAR(64), nullable=False, comment='지갑 내역 타입 (입금/출금/환전 등)')
    transactionComment = Column(VARCHAR(32), nullable=False, comment='지갑 내역 적요')
    transactionId = Column(BigInteger, nullable=False, comment='지갑 내역 타입 id')
    transactionDate = Column(Date, nullable=False, comment='이체 일')
    transactionTime = Column(Time, nullable=False, comment='이체 시간')
    amount = Column(DECIMAL(12, 3), nullable=False, default=0.000, comment='금액')
    afterBalance = Column(DECIMAL(18, 3), nullable=False, default=0.000, comment='잔액')
    settlementRate = Column(DECIMAL(12, 3), nullable=False, default=1.000, comment='체결 환율')
    averageRate = Column(DECIMAL(12, 3), default=0.000, comment='평균매매율')
    averageRate2 = Column(DECIMAL(12, 3), nullable=False, default=0.000, comment='평균매매율2')
    settlementProfit = Column(DECIMAL(18, 3), nullable=False, default=0.000, comment='매도 시 확정 수익금')
    contrastPercentage = Column(DECIMAL(18, 3), nullable=False, default=0.000, comment='환전 매도 수익률')
    createdAt = Column(DateTime, nullable=False, server_default=func.now(), comment='생성일자')
    updatedAt = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(), comment='수정일자')

    def to_string(self):
        return (
            f"WalletBlockTransaction(id={self.id}, walletId={self.walletId}, "
            f"transactionType='{self.transactionType}', transactionComment='{self.transactionComment}', "
            f"transactionId={self.transactionId}, transactionDate={self.transactionDate}, "
            f"transactionTime={self.transactionTime}, amount={self.amount}, "
            f"afterBalance={self.afterBalance}, settlementRate={self.settlementRate}, "
            f"averageRate={self.averageRate}, averageRate2={self.averageRate2}, "
            f"settlementProfit={self.settlementProfit}, contrastPercentage={self.contrastPercentage}, "
            f"createdAt={self.createdAt}, updatedAt={self.updatedAt})"
        )
