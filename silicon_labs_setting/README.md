# Silicon Labsの Simplicity Studioの日本語版


## Generic Access
Generic Access : generic_accessサービスは，デバイスに関する一般的な情報を含み，利用可能なすべての特性を読み取り可能．
Appearance : このデバイスの見た目．値はカテゴリとサブカテゴリに分かれる

## Device Information
Serial Number Studio: デバイスの特定のインスタンスのシリアル番号を示す可変長のUTF-8文字列

Hardware Revision String: 装置内のハードウェアのハードウェアリビジョンを表すUTF-8文字列

Firmware Revision String: 装置内のファームウェアのファームウェアリビジョンを表すUTF-8文字列

Software Revision String: 装置内のソフトウェアのソフトウェアリビジョンを表すUTF-8文字列

SystemID: Bluetooth Device Addressを元にIDを生成する場合は，BluetoothDeviceAddressは48ビットで，24ビットのCompany assigned identifierと24ビットのCompany 

identifierを連結した構造になっている． Bluetooth Device AddressをシステムIDとしてカプセル化をするには，Company identifierに0XFFFFを連結し，Bluetooth Addressの

Company Assigned identifierを連結してください．

IEEE 11073-20601 Regulatory Certicationb Data List: デバイスが準拠を主張する様々な規制および/または認証コンプライアンス項目を列挙した不透明な構造体である．この特性の内容は，Certificationを提供するAuthorizing Organizationによって決定される．このリストのフォーマットに関する詳細については，11073-20601またはContinua Design Guidelinesを参照してください．

PnP ID: PnP特性は，GATT特性Value Read手順で読み出すと，その値を返す． PnP_ID特性は，このデバイスのためにユニークであるデバイスID値を作成するために使用される値のセットである．この特性には，Vendor ID sourceフィールド，Vendor IDフィールド，Product IDフィールド， Product Versionフィールドが含まれる．これらの値は，特定のタイプ/モデル/バージョンのすべてのデバイスを番号で識別するために使用される．

## Battery Service
### Battery Level: バッテリーの現在の充電レベルを表す．0~100%の充電状態を表す
Characteristic Presentation Format: 特性値の形式を定義する． 1つ以上の特性表示形式記述子が存在する可能性がある．これらの記述が複数存在する場合，Aggregate Formate記述子が存在することになる． この記述子は読み取り専用であり，読み取りに認証や許可を必要としない．この記述子は，形式，指数，単位，名前，スペース，説明の5つん部分から構成される．

## Environment Sensing
### Descrip